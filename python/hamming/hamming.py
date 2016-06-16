#
# Solution for hamming
# Written by Sofia Nieves
# Thu 16 Jun 05:27:50 UTC 2016
#

def distance(strand1, strand2):
    # Return nonsensical number if strands are different lengths
    if len(strand1) != len(strand2):
        return -1

    distance = 0

    for position, nucleotide in enumerate(strand1):
        if strand1[position] != strand2[position]:
            distance += 1

    return distance
