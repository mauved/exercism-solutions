
# Solution for isogram

import string

def is_isogram(word):

    for letter in word.lower():
        if letter in string.ascii_lowercase and word.lower().count(letter) > 1:
            return False
    return True
