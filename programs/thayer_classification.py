import csv

temp_list = []
valence_str = ""
arousal_str = ""
mood_str = ""
valence_list = []
arousal_list = []
mood_list = []
valence_mean = 0.0
arousal_mean = 0.0


def classify_mood(valence, arousal):
    # quadrant 1 analysis
    if ((valence >= 6.1 and 4.8 <= arousal < 5.9) or (valence >= 7.3 and 5.9 <= arousal < 7)):
        return 'pleased'
    elif ((4.9 <= valence < 6.1 and 4.8 <= arousal < 5.9) or (6.1 <= valence < 7.3 and 5.9 <= arousal < 7) or
          (7.3 <= valence and arousal >= 7)):
        return 'happy'
    elif ((4.9 <= valence < 7.3 and arousal >= 7) or (4.9 <= valence < 6.1 and 5.9 <= arousal < 7)):
        return 'excited';
    # quadrant 2 analysis
    elif ((2.7 <= valence < 4.9 and 7 <= arousal) or (3.8 <= valence < 4.9 and 5.9 <= arousal < 7)):
        return 'annoyed'
    elif ((3.8 <= valence < 4.9 and 4.8 <= arousal < 5.9) or (2.7 <= valence < 3.8 and 5.9 <= arousal < 7) or
          (2.7 > valence and arousal >= 7)):
        return 'angry'
    elif ((valence < 3.8 and 4.8 <= arousal < 5.9) or (valence < 2.7 and 5.9 <= arousal < 7)):
        return 'nervous';
    # quadrant 3 analysis
    elif ((valence < 3.8 and 3.8 <= arousal < 4.8) or (valence < 2.7 and 2.7 <= arousal < 3.8)):
        return 'sad'
    elif ((3.8 <= valence < 4.9 and 3.8 <= arousal < 4.8) or (2.7 <= valence < 3.8 and 2.7 <= arousal < 3.8) or
          (2.7 > valence and arousal > 2.7)):
        return 'bored'
    elif ((2.7 <= valence < 4.9 and arousal < 2.7) or (3.8 <= valence < 4.9 and 2.7 <= arousal < 3.8)):
        return 'sleepy';
    # quadrant 4 analysis
    elif ((valence >= 6.1 and 3.8 <= arousal < 4.8) or (valence >= 7.3 and 3.8 <= arousal < 4.8)):
        return 'relaxed'
    elif ((4.9 <= valence < 6.1 and 3.8 <= arousal < 4.8) or (6.1 <= valence < 7.3 and 2.7 <= arousal < 3.8) or
          (7.3 <= valence and arousal < 2.7)):
        return 'peaceful'
    elif ((4.9 <= valence < 7.3 and arousal < 2.7) or (4.9 <= valence < 7.3 and 2.7 <= arousal < 3.8)):
        return 'calm';
    # error catching
    else:
        return 'error'


print('Music Evaluation Software; Mel Mark; Park University; Fall 2019\n')

# opening table of valence and arousal means
with open('table.csv', 'r') as f:
    reader = csv.reader(f)
    temp_list = list(reader)
f.close()
# storing them in lists
for x in temp_list:
    valence_str += x[1] + ', '
    arousal_str += x[2] + ', '
valence_list = valence_str.split(', ')
arousal_list = arousal_str.split(', ')
# deleting the column names and extra blank
del valence_list[0]
del arousal_list[0]
del valence_list[1744]
del arousal_list[1744]
valence_list = [float(i) for i in valence_list]
arousal_list = [float(i) for i in arousal_list]
# classifying the moods and appending to big string
for z in range(1744):
    mood_str += classify_mood(valence_list[z], arousal_list[z]) + ', '
# converting big string to a more manageable list
mood_list = mood_str.split(', ')
del mood_list[1744]
print(len(valence_list), 'values; valence list:\t', valence_list)
print(len(arousal_list), 'values; arousal list:\t', arousal_list)
print(len(mood_list), 'values; mood list:\t', mood_list)
for i in range(len(mood_list)):
    print(mood_list[i])

