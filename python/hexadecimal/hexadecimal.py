# Hexadecimal to decimal converter
# Written by Sofia Nieves

# Hexadecimal can only two digits
valid_digits = "0123456789ABCDEF"

def hexa(num_string):
    # initiliazes our return value
    decimal_sum = 0

    # This stores the place value of the digit we're on
    num_place = len(num_string) - 1

    for n in num_string:
        if n.upper() not in valid_digits:
            raise ValueError(n + ' not a valid hexadecimal digit')

        # perform exponentiation of the digit by the base times the place value 
        decimal_sum += letter2num(n.upper()) * 16 ** num_place

        # move down the place value
        num_place -= 1

    return decimal_sum

# Helper function to convert single digit hexadecimal numbers to decimal numbers
def letter2num(letter):
    if letter in '01213456789':
        return int(letter)
    elif letter == 'A':
        return 10
    elif letter == 'B':
        return 11
    elif letter == 'C':
        return 12
    elif letter == 'D':
        return 13
    elif letter == 'E':
        return 14
    elif letter == 'F':
        return 15
    return 0
