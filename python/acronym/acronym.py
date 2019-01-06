import re


def abbreviate(words):
    abbreviation = ''

    # Any sequence of "word" characters and apostrophes is considered a word
    word_list = re.findall(r"[\w']+", words)

    for word in word_list:
        abbreviation += word[:1].upper()

    return abbreviation
