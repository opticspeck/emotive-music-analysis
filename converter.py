# Written by Mel Mark, Park University 2019, to convert JSON files to ARFF files for the ML app, Weka.
# https://m3l.me

import json

just_nums = ""
end_str = ""
list_of_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_mums_and_dot = list_of_nums + ['.']

with open('file_to_read.json') as json_file:
    json_data = json.load(json_file)
    json_values_as_list = json_data.values()
    values = str(json_values_as_list)
    for x in range(len(values)):
        if values[x] in list_of_nums and values[x + 1] == ',':
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
