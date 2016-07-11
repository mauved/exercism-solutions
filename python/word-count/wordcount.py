#
# Solution for wordcount
# Written by Sofia Nieves
# Not really sure what to make of the unicode yet
#

import string

def word_count(phrase):
    word_count = {}

    # Translation table of punctuation to white space
    punct_remove = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    clean_phrase = phrase.translate(punct_remove)

    word_list = clean_phrase.lower().split()

    word_list = [ word.strip() for word in word_list ]

    for word in word_list:
        word_count[word] = word_list.count(word)

    if '' in word_count:
        del word_count['']

    return word_count
