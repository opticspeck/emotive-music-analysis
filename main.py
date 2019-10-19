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
valence_mean = float(input('What is the valence mean?\t'))
arousal_mean = float(input('What is the arousal mean?\t'))
mood = classify_mood(valence_mean, arousal_mean)
print('I predict the mood of this song is: ', mood)
