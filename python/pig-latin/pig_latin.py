# Solution for Pig Latin

VOWELS = 'aeiouAEIOU'
VOWELEXCEPTIONS = ['yt', 'xr']
EXCEPTIONS2 = ['th', 'qu', 'sh', 'ch']
EXCEPTIONS3 = ['squ', 'thr', 'sch']

def translate(en_word):

    # Check for exceptions first
    if en_word[:3] in EXCEPTIONS3:
        return en_word[3:] + en_word[:3] + 'ay'
    
    if en_word[:2] in EXCEPTIONS2:
        return en_word[2:] + en_word[:2] + 'ay'

    if en_word[:2] in VOWELEXCEPTIONS:
        return en_word + 'ay'

    # These are the simple cases
    if en_word[:1] in VOWELS:
        return en_word + 'ay'
    if en_word[:1] not in VOWELS:
        return en_word[1:] + en_word[:1] + 'ay'
