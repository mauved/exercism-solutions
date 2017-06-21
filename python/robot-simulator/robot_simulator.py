class Robot(object):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    def __init__(self):
        self.coordinates = (0, 0)
        self.bearing = NORTH
        pass

    def turn_left():
        if self.bearing == NORTH:
            self.bearing = WEST
        elif self.bearing == SOUTH:
            self.bearing = EAST
        elif self.bearing == WEST:
            self.bearing = SOUTH
        elif self.bearing == EAST:
            self.bearing = NORTH
        pass

    def turn_right():
        if self.bearing == NORTH:
            self.bearing = EAST
        elif self.bearing == SOUTH:
            self.bearing = WEST
        elif self.bearing == WEST:
            self.bearing = NORTH
        elif self.bearing == EAST:
            self.bearing = SOUTH
        pass

    def advance():
        current_coords = self.coordinates
        if self.bearing == NORTH:
            self.coordinates = (current_coords[0], current_coords[1] + 1)
        elif self.bearing == SOUTH:
            self.coordinates = (current_coords[0], current_coords[1] - 1)
        elif self.bearing == WEST:
            self.coordinates = (current_coords[0] - 1, current_coords[1])
        elif self.bearing == EAST:
            self.coordinates = (current_coords[0] + 1, current_coords[1])
        pass

    def simulate(instructions):
        for step in instructions:
            
        pass
