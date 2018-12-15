class Direction:
    """Class representing a direction in 2D world."""
    UP = 8
    DOWN = 2
    LEFT = 4
    RIGHT = 6
    NOT_MOVING = 5
    VERTICAL = 1
    HORIZONTAL = 0
    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)


class Car:
    """ A class representing a car in rush hour game.
    A car is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A car drives on its vertical\horizontal axis back and
    forth until reaching the board's boarders. A car can only drive to an empty
    slot (it can't override another car)."""

    def __init__(self, color, length, location, orientation):
        """A constructor for a Car object
        :param color: A string representing the car's color
        :param length: An int in the range of (2,4) representing the car's length.
        :param location: A list representing the car's head (x, y) location
        :param orientation: An int representing the car's orientation"""
        self.color = color
        self.length = length
        self.location = location
        self.orientation = orientation

    def __str__(self):
        return self.color + ": " + str(self.location) + str(self.orientation)
