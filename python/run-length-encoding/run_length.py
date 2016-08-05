# Solution for run length
# Written by Sofia Nieves


def encode(word):
    #for character in encoded_word:
        
    return ''

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

