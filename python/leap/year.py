#
# Solution file for Python "Leap" exercise
# Solution by Sofia Nieves
# Thu 26 May 08:41:09 UTC 2016
#

def is_leap_year(yr=0):
    return (yr % 4 == 0) and ((yr % 100 != 0) or (yr % 400 == 0))
