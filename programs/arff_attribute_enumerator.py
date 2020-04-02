# Written by Mel Mark, Park University 2019
# A tool to help me out generating lots of lines of attributes for the converter outline.
# https://m3l.me

repeat = "n"
name_of_attribute = ""
# attributes that have the most common set of variables (see following list)
normal_attributes = [
    "barkbands",
    "erbbands",
    "melbands",
    "melbands128",
    "spectral_contrast_coeffs",
    "spectral_contrast_valleys",
    "beats_loudness_band_ratio",
    "hpcp",
    "hpcp_crest",
]
normal_variables = [
    "dmean",
    "dmean2",
    "dvar",
    "dvar2",
    "max",
    "mean",
    "median",
    "min",
    "stdev",
    "var",
]
# attributes that only have itself :(
lonely_attributes = ["beats_position", "bpm_histogram", "chords_histogram", "thpcp"]
# attributes that have the same set of three variables (see following list)
cc_attributes = ["gfcc", "mfcc"]
cc_variables = ["mean", "cov", "icov"]


def generate_normal_attributes(variable_name):
    if number_of_commas > 0:
        for x in range(number_of_commas + 1):
            print(
                "@attribute     "
                + type_of_attribute
                + "."
                + name_of_attribute
                + "."
                + variable_name
                + "_"
                + str(x)
                + "    REAL"
            )
    else:
        print(
            "@attribute     "
            + type_of_attribute
            + "."
            + name_of_attribute
            + "."
            + variable_name
            + "    REAL"
        )


def generate_cc_attributes(
    number_of_mean_commas, number_of_cov_commas, number_of_icov_commas
):
    for x in range(number_of_mean_commas):
        print(
            "@attribute     "
            + type_of_attribute
            + "."
            + name_of_attribute
            + ".mean_"
            + str(x)
            + "    REAL"
        )
    for x in range(number_of_cov_commas):
        print(
            "@attribute     "
            + type_of_attribute
            + "."
            + name_of_attribute
            + ".cov_"
            + str(x)
            + "    REAL"
        )
    for x in range(number_of_icov_commas):
        print(
            "@attribute     "
            + type_of_attribute
            + "."
            + name_of_attribute
            + ".icov_"
            + str(x)
            + "    REAL"
        )


beats_pos = input("how many beats positions\t")
count = 118 - int(beats_pos)
bleh = ""
for x in range(count):
    if x != count - 1:
        bleh += "0, "
    else:
        bleh += "0"
print(bleh)

while repeat == "y":
    type_of_attribute = input("what type of attribute is it? (ll/r/t)\t")
    name_of_attribute = input("name of attribute?\t")
    name_of_attribute = name_of_attribute.lower()

    if type_of_attribute == "ll":
        type_of_attribute = "lowlevel"
    elif type_of_attribute == "r":
        type_of_attribute = "rhythm"
    elif type_of_attribute == "t":
        type_of_attribute = "tonal"
    else:
        print("invalid type of attribute >:(")
        break

    if name_of_attribute in normal_attributes:
        number_of_commas = int(input("how many commas are there?\t"))
        for x in range(len(normal_variables)):
            generate_normal_attributes(normal_variables[x])
    elif name_of_attribute in lonely_attributes:
        number_of_commas = int(input("how many commas are there?\t"))
        for x in range(number_of_commas):
            print(
                "@attribute     "
                + type_of_attribute
                + "."
                + name_of_attribute
                + "."
                + "_"
                + str(x)
                + "    REAL"
            )
    elif name_of_attribute in cc_attributes:
        number_of_mean_commas = int(input("how many MEAN commas are there?\t"))
        number_of_cov_commas = int(input("how many COV commas are there?\t"))
        number_of_icov_commas = int(input("how many ICOV commas are there?\t"))
        for x in range(3):
            generate_cc_attributes(
                number_of_mean_commas, number_of_cov_commas, number_of_icov_commas
            )
    else:
        print("invalid attribute name >:(")
        break

    repeat = input("do you have more to enumerate? y/n\t")
print("thanks for using! check out my website: https://m3l.me ^-^")
