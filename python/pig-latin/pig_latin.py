# Solution for Pig Latin

VOWELS = 'AEIOU'

def translate(en_word):
    if en_word[:1] in VOWELS:
        return en_word + 'ay'
    if en_word[:1] not in VOWELS:
        return en_word[1:] + en_word[:1] + 'ay'
