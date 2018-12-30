import re


def abbreviate(words):
    abbreviation = ''

    # Any sequence of "word" characters and apostrophes is considered a word
    split_word = re.findall(r"[\w']+", words)

    for components in split_word:
        abbreviation += components[:1].upper()

    return abbreviation
