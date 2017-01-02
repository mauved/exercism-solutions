#
# Solution for clock in Python
# Written by Sofia Nieves
#

class Clock:
    """This is a simple clock that just keeps track of the hour and minute."""

    def __init__(self, hours, minutes):
        self.hour = hours
        self.minute = minutes

    def __repr__(self):
        self.normalize()
        return '{0:02d}:{1:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        if (self.__repr__() == other.__repr__()):
            return True
        else:
            return False

    def add(self, add_mins):
        """Add minutes to the clock"""
        self.minute += add_mins
        return self.__repr__()

    def normalize(self):
        """
        Brings clock down to normal 0-23, 0-59 range
        """
        self.extra_hours = (self.minute // 60)
        self.hour += self.extra_hours
        self.hour %= 24
        self.minute %= 60

