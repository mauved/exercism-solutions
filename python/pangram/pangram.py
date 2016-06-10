#
# Solution file for problem "Pangram"
# Written by Sofia Nieves
# Fri 10 Jun 19:30:47 UTC 2016
# Written for English pangrams
#

import string

def is_pangram(phrase=''):
    # Remove special characters by converting to ASCII
    new_phrase = ascii(phrase)

    # Add character to set if it's in the alphabet
    char_set = set()
    for char in new_phrase:
        if char.isalpha():
            # Convert to uppercase before adding to set
            char_set.add(char.upper())

    if len(char_set) == 26:
        return True

    return False
