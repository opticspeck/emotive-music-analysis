# Written by Mel Mark, Park University 2019, to convert JSON files to ARFF files for the ML app, Weka.
# https://m3l.me

import json

just_nums = ""
end_str = ""

with open('file_to_read.json') as json_file:
    json_data = json.load(json_file)
    json_values_as_list = json_data.values()
    values = str(json_values_as_list)
    for x in range(len(values)):
        if (values[x] == '0' and values[x + 1] == ',') or (values[x] == '1' and values[x + 1] == ',') or \
                (values[x] == '2' and values[x + 1] == ',') or (values[x] == '3' and values[x + 1] == ',') or \
                (values[x] == '4' and values[x + 1] == ',') or (values[x] == '5' and values[x + 1] == ',') or \
                (values[x] == '6' and values[x + 1] == ',') or (values[x] == '7' and values[x + 1] == ',') or \
                (values[x] == '8' and values[x + 1] == ',') or (values[x] == '9' and values[x + 1] == ','):
            just_nums += values[x] + ', '
        elif (values[x] == '0' or values[x] == '1' or values[x] == '2' or values[x] == '3' or values[x] == '4' or
              values[x] == '5' or values[x] == '6' or values[x] == '7' or values[x] == '8' or values[x] == '9' or
              values[x] == '.'):
            just_nums += values[x]
        elif (values[x] == 'e' and values[x + 1] == '+') or (values[x] == 'e' and values[x + 1] == '-'):
            just_nums += values[x] + values[x + 1]
        # appending the end with the key signature
        elif values[x] == 'd' and values[x + 1] == 's' and values[x + 2] == '_' and values[x + 3] == 'k' and \
                values[x + 4] == 'e':
            just_nums += ", '" + values[x + 10] + "', "
        # appending the end with whether the key signature is a major/minor key
        elif values[x] == 'd' and values[x + 1] == 's' and values[x + 2] == '_' and values[x + 3] == 's' and values[
            x + 4] == 'c':
            just_nums += "'" + values[x + 12] + values[x + 13] + values[x + 14] + values[x + 15] + values[x + 16] + "'"

    print(json_data, "\n")
    print(json_values_as_list, "\n")
    print(values, "\n")
    print(just_nums)
