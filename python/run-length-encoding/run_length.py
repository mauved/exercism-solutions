# Solution for run length
# Written by Sofia Nieves

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

    return encoded_word

def decode(encoded_word):
    decoded_word = ''
    count = 0

    for character in encoded_word:
        if count <= 0:
            count = int(character)
            continue

        while count > 0:
            decoded_word += character
            count -= 1

    return decoded_word

