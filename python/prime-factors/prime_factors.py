#
# Solution for Prime Factors
# Written by Sofia Nieves
#

def prime_factors(dividend):
    factors = []
    divisor = 2
    result = dividend

    # Continue until result is smaller than divisor
    while result >= divisor:
        if result % divisor == 0:
            factors.append(divisor)
            result /= divisor
        else:
            divisor += 1

    return factors
