# Solution for run length
# Written by Sofia Nieves


def encode(word):
    encoded_word = ''
    previous_character = word[0]
    character_count = 0

    for character in word:
        if character == previous_character:
            character_count += 1
        else:
            if character_count == 1:
                encoded_word += previous_character
            else:
                encoded_word += str(character_count) + previous_character

            previous_character = character
            character_count = 1
    
    if character_count == 1:
        encoded_word += previous_character
    else:
        encoded_word += str(character_count) + previous_character

    return encoded_word

def decode(encoded_word):
    decoded_word = ''
    expand_char = ''
    for character, position in encoded_word:
        if number_characters == 0:
            number_characters = int(character)
            continue
        expand_char = character

        while number_characters > 0:
            decoded_word += expand_char
            number_characters -= 1
            
    return decoded_word

