def translate_word(word):
    if (word[0] in 'aeiuo' or (word[0:2] == 'xr') or (word[0:2] == 'yt')):
        word = word + 'ay'

    elif (word[1:3] == 'qu'):
        word = word[3:] + word[0:1] + 'quay'

    elif (word[0:2] == 'qu'):
        word = word[2:] + 'quay'

    elif (word[0] in 'qwrtpsdfghjklzxcvbnm' and word[1] in 'qwrtpsdfghjklzxcvbnm' and word[2] in 'qwrtpsdfghjklzxcvbnm'):
        word = word[3:] + word[0:3] + 'ay'

    elif (word[0] in 'qwrtpsdfghjklzxcvbnm' and word[1] in 'qwrtpsdfghjklzxcvbnm' and word[2] == 'y'):
        word = word[2:] + word[0:2] + 'ay'

    elif (word[0] in 'qwrtpsdfghjklzxcvbnm' and word[1] in 'qwrtpsdfghjklzxcvbnm'):
        word = word[2:] + word[0:2] + 'ay'

    else:
        word = word[1:] + word[0] + 'ay'

    return word


def translate(text):
    words = text.split()
    results = []
    for word in words:
        results.append(translate_word(word))
    return " ".join(results)