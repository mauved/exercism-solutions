# Binary to decimal converter
# Written by Sofia Nieves

# Binary can only two digits
valid_values = "01"

def parse_binary(num_string):
    # initiliazes our return value
    decimal_sum = 0

    # This stores the place value of the digit we're on
    num_place = len(num_string) - 1

    for n in num_string:
        if n not in valid_values:
            raise ValueError(n + ' not a valid binary digit')

        # perform exponentiation of the digit by the base times the place value 
        decimal_sum += int(n) * 2 ** num_place

        # move down the place value
        num_place -= 1

    return decimal_sum

