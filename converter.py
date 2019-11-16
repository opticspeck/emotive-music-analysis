# Written by Mel Mark, Park University 2019
# A tool to convert JSON files to ARFF files for the machine learning app, Weka.
# https://m3l.me

import json

header = ""
just_nums = ""
end_str = ""
list_of_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_mums_and_dot = list_of_nums + ['.']

with open('file_to_read.json') as json_file:
    json_data = json.load(json_file)
    json_values_as_list = json_data.values()
    values = str(json_values_as_list)
    for x in range(len(values)):
        # this accounts for an issue I found when collecting the metadata information since digits can exist in
        # non-numerical variables like strings. this is not a very elegant way of going about it but it should work
        # since bpms should be between 1-3 digits.
        if values[x] == 'u' and values[x + 1] == 'n' and values[x + 2] == 't':
            if (values[x + 5] == ' ' and values[x + 6] in list_of_nums and values[x + 7] == ',') or\
                    (values[x + 5] == ' ' and values[x + 6] in list_of_nums and values[x + 7] in list_of_nums and
                     values[x + 8] == ',') or (values[x + 5] == ' ' and values[x + 6] in list_of_nums and
                                               values[x + 7] in list_of_nums and values[x + 8] in list_of_nums and
                                               values[x + 9] == ','):
                just_nums += ', '
        elif values[x] in list_of_nums and (values[x + 1] == ',' or values[x + 1] == '}' or values[x + 1] == ']'):
            just_nums += values[x] + ', '
        elif values[x] in list_of_mums_and_dot:
            just_nums += values[x]
        elif (values[x] == 'e' and values[x + 1] == '+') or (values[x] == 'e' and values[x + 1] == '-'):
            just_nums += values[x] + values[x + 1]
        # appending the end with the key signature
        elif values[x] == 'd' and values[x + 1] == 's' and values[x + 2] == '_' and values[x + 3] == 'k' and \
                values[x + 4] == 'e':
            # this accounts for keys that are flat (b) or sharp (#)
            if values[x + 5] == 'b' or '#':
                just_nums += ", '" + values[x + 10] + values[x + 11] + "', "
            else:
                just_nums += ", '" + values[x + 10] + "', "
        # appending the end with whether the key signature is a major/minor key
        # (lucky that both 'major' and 'minor' hve 5 characters)
        elif values[x] == 'd' and values[x + 1] == 's' and values[x + 2] == '_' and values[x + 3] == 's' and values[
            x + 4] == 'c':
            just_nums += "'" + values[x + 12] + values[x + 13] + values[x + 14] + values[x + 15] + values[x + 16] + "'"

    print(json_data, "\n")
    print(json_values_as_list, "\n")
    print(values, "\n")
    print(just_nums)
