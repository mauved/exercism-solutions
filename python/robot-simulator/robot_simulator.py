# Robot bearing definitions
NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"


class Robot(object):

    def __init__(self, bearing=None, x=None, y=None):
        """ Default bearing for robot is facing north at coordinates (0, 0) """
        if bearing is None:
            self.bearing = NORTH
        else:
            self.bearing = bearing
        if x is None and y is None:
            self.coordinates = (0, 0)
        else:
            self.coordinates = (x, y)

    def turn_left(self):
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == EAST:
            self.bearing = NORTH

    def turn_right(self):
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH
        elif self.bearing == EAST:
            self.bearing = SOUTH

    def advance(self):
        if self.bearing == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.bearing == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        elif self.bearing == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
        elif self.bearing == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])

    def simulate(self, instructions):
        """ Any instructions given other than advance, turn left, turn right are
        ignored
        """
        for step in instructions:
            if step == "A":
                self.advance()
            elif step == "L":
                self.turn_left()
            elif step == "R":
                self.turn_right()
