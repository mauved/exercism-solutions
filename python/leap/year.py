#
# Solution file for Python "Leap" exercise
# Solution by Sofia Nieves
# Thu 26 May 08:41:09 UTC 2016
#

def is_leap_year(yr=0):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            return False
        return True
    return False
