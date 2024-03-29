# Written by Mel Mark, Park University 2019
# A tool to convert JSON files to ARFF files for the machine learning app, Weka.
# https://m3l.me

import json
from shutil import copyfile

new_file_name = "birthofcreation"
header = ""
just_nums = ""
end_str = ""
filtered_string = ""
list_of_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list_of_mums_and_separators = list_of_nums + ["."] + ["-"]

with open(new_file_name + ".json") as json_file:
    json_data = json.load(json_file)
    json_values_as_list = json_data.values()
    values = str(json_values_as_list)
    for x in range(len(values)):
        # this accounts for an issue I found when collecting the metadata information since digits can exist in
        # non-numerical variables like strings. this is not a very elegant way of going about it but it should work
        # since bpms should be between 1-3 digits.
        if values[x] == "u" and values[x + 1] == "n" and values[x + 2] == "t":
            if (
                (
                    values[x + 5] == " "
                    and values[x + 6] in list_of_nums
                    and values[x + 7] == ","
                )
                or (
                    values[x + 5] == " "
                    and values[x + 6] in list_of_nums
                    and values[x + 7] in list_of_nums
                    and values[x + 8] == ","
                )
                or (
                    values[x + 5] == " "
                    and values[x + 6] in list_of_nums
                    and values[x + 7] in list_of_nums
                    and values[x + 8] in list_of_nums
                    and values[x + 9] == ","
                )
            ):
                just_nums += ", "
        # getting rid of var2, dmean2, loudness_ebu128, silence_rate_20dB, silence_rate_30dB, silence_rate_60dB,
        # and melbands128
        elif (
            (values[x - 1] == "r" and values[x] == "2" and values[x + 1] == "'")
            or (values[x - 1] == "n" and values[x] == "2" and values[x + 1] == "'")
            or (values[x - 1] == "u" and values[x] == "1" and values[x + 1] == "2")
            or (
                values[x - 2] == "u"
                and values[x - 1] == "1"
                and values[x] == "2"
                and values[x + 1] == "8"
            )
            or (
                values[x - 3] == "u"
                and values[x - 2] == "1"
                and values[x - 1] == "2"
                and values[x] == "8"
                and values[x + 1] == "'"
            )
            or (values[x - 1] == "_" and values[x] == "2" and values[x + 1] == "0")
            or (values[x - 1] == "2" and values[x] == "0" and values[x + 1] == "d")
            or (values[x - 1] == "_" and values[x] == "3" and values[x + 1] == "0")
            or (values[x - 1] == "3" and values[x] == "0" and values[x + 1] == "d")
            or (values[x - 1] == "_" and values[x] == "6" and values[x + 1] == "0")
            or (values[x - 1] == "6" and values[x] == "0" and values[x + 1] == "d")
            or (values[x - 1] == "s" and values[x] == "1" and values[x + 1] == "2")
            or (
                values[x - 2] == "s"
                and values[x - 1] == "1"
                and values[x] == "2"
                and values[x + 1] == "8"
            )
            or (
                values[x - 3] == "s"
                and values[x - 2] == "1"
                and values[x - 1] == "2"
                and values[x] == "8"
                and values[x + 1] == "'"
            )
        ):
            just_nums += "DEL, "

        elif values[x] in list_of_nums and (
            values[x + 1] == "," or values[x + 1] == "}" or values[x + 1] == "]"
        ):
            just_nums += values[x] + ", "
        # accounting for e+ and e- values
        elif (values[x] == "e" and values[x + 1] == "+") or (
            values[x] == "e" and values[x + 1] == "-"
        ):
            just_nums += values[x] + values[x + 1]
        elif values[x] in list_of_mums_and_separators:
            if values[x - 1] != "e" and values[x + 1] != "-":
                just_nums += values[x]
        # appending the end with the key signature
        elif (
            values[x] == "d"
            and values[x + 1] == "s"
            and values[x + 2] == "_"
            and values[x + 3] == "k"
            and values[x + 4] == "e"
        ):
            # this accounts for keys that are flat (b) or sharp (#)
            if values[x + 5] == "b" or values[x + 5] == "#":
                just_nums += ", '" + values[x + 10] + values[x + 11] + "', "
            else:
                just_nums += ", '" + values[x + 10] + "', "
        # appending the end with whether the key signature is a major/minor key
        # (lucky that both 'major' and 'minor' hve 5 characters)
        elif (
            values[x] == "d"
            and values[x + 1] == "s"
            and values[x + 2] == "_"
            and values[x + 3] == "s"
            and values[x + 4] == "c"
        ):
            just_nums += (
                "'"
                + values[x + 12]
                + values[x + 13]
                + values[x + 14]
                + values[x + 15]
                + values[x + 16]
                + "'"
            )

    just_nums_as_list = just_nums.split(", ")
    # deleting trash values
    while "DEL" in just_nums_as_list:
        index = just_nums_as_list.index("DEL")
        del just_nums_as_list[index]
    # removes weird blank element
    del just_nums_as_list[-3]
    # removes beats positions
    number_of_beats_position = len(just_nums_as_list) - 4377
    end_of_delete = 3666 + number_of_beats_position
    del just_nums_as_list[3666:end_of_delete]

    for x in range(len(just_nums_as_list)):
        # the actual number generated by Essentia should be less than 25 digits (including '.', 'e+', and 'e-')
        # the compounded conditional just removes the trailing comma
        if len(just_nums_as_list[x]) <= 25 and x != len(just_nums_as_list) - 1:
            filtered_string += str(just_nums_as_list[x]) + ", "
        elif len(just_nums_as_list[x]) <= 25:
            filtered_string += str(just_nums_as_list[x])

    print("raw json data:                ", json_data)
    print("json data as list:            ", json_values_as_list)
    print("json data as a string:        ", values)
    print("just the numbers as a string: ", just_nums)
    print("just the numbers as list:     ", just_nums_as_list)
    print("filtered numbers as string:   ", filtered_string)

    # outputting to new file for weka
    new_file_name += ".arff"
    copyfile("base_first.arff", new_file_name)
    f = open(new_file_name, "a+")
    j = open("base_second.arff", "r")
    data = j.read()
    j.close()
    f.write(data)
    f.write(filtered_string)
    f.close()
