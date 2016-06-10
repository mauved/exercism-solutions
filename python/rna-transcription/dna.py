#
# Solution file for rna transcription
# Written by Sofia Nieves
# Fri 10 Jun 20:06:53 UTC 2016
#

def to_rna(strand):
    complement = ''
    adenine = 'A'
    cytosine = 'C'
    guanine = 'G'
    thymine = 'T'
    uracil = 'U'

    for nucleotide in strand:
        if nucleotide == guanine:
            complement = complement + cytosine
        elif nucleotide == cytosine:
            complement = complement + guanine
        elif nucleotide == thymine:
            complement = complement + adenine
        elif nucleotide == adenine:
            complement = complement + uracil

    return complement
