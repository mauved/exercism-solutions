import math


def sieve(limit):

    # If the number's too small there are no primes to check for
    if limit < 2:
        return []

    worklist = range(2, limit + 1)
    primes = []
    notprimes = []

    for i in worklist:
        # Assume i is prime if not marked as nonprime
        if i not in notprimes:
            primes.append(i)

            # All nonprimes will be marked after
            # iterating past square root of limit
            if i <= int(math.sqrt(limit)):
                # Mark multiples of prime as nonprime
                for j in range(i**2, limit + 1, i):
                    notprimes.append(j)

    return primes
