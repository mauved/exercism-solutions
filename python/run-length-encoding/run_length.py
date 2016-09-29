# Solution for run length
# Written by Sofia Nieves

import string

def encode(word):
    encoded_word = ''
    previous_character = word[0]
    character_count = 0

    # if the current character matches previous character increment counter
    # if not, append our count and the character
    for character in word:
        if character == previous_character:
            character_count += 1
        else:
            # If the character only occurs once, the character is appended by
            # itself e.g. AAB becomes 2AB and not 2A1B
            if character_count == 1:
                encoded_word += previous_character
            else:
                encoded_word += str(character_count) + previous_character

            # reinitialize counter and set previous character
            previous_character = character
            character_count = 1
    
    if character_count == 1:
        encoded_word += previous_character
    else:
        encoded_word += str(character_count) + previous_character

    return encoded_word

def decode(encoded_word):
    decoded_word = ''
    count = ''

    # If the character's a number append it
    # If it isn't, use the number to repeat the character
    for character in encoded_word:
        if character not in string.digits:

            # If we don't have a number the character is only listed once
            if count == '':
                count = 1
            else:
                count = int(count)
            
            # append character
            for _ in range(count):
                decoded_word += character

            count = ''
            continue

        count += character

    return decoded_word

