#
# Solution for wordcount
# Written by Sofia Nieves
#
#

import string


def word_count(phrase):
    word_list = phrase.strip(string.punctuation).lower().split()
    word_count = {}

    for word in word_list:
        word_count[word] = word_list.count(word)

    return word_count
