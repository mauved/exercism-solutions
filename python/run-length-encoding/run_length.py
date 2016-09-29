# Solution for run length
# Written by Sofia Nieves

<<<<<<< HEAD
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
=======
def encode(word):
    encoded_word = ''
    count = 0
    previous_character = str(word[0])

    for character in word:
        if character == previous_character:
            count += 1
        else:
            encoded_word += str(count) + str(previous_character)
            previous_character = character
            count = 1
    encoded_word += str(count) + str(previous_character)
>>>>>>> 3f60f72f507b30317f473e0921782a853c8bf7e5

    return encoded_word

def decode(encoded_word):
    decoded_word = ''
<<<<<<< HEAD
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
=======
    count = 0

    for character in encoded_word:
        if count <= 0:
            count = int(character)
            continue

        while count > 0:
            decoded_word += character
            count -= 1
>>>>>>> 3f60f72f507b30317f473e0921782a853c8bf7e5

    return decoded_word

