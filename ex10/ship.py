

class Ship():

    SHIP_RADIUS = 1
    FULL_LIVES = 3

    def __init__(self, location):
        self.__location = location
        self.__speed = [0,0]
        self.__direction = 0
        self.__lives = self.FULL_LIVES

    def get_speed(self ):
        return self.__speed

    def get_location(self):
        return self.__location

    def get_direction(self):
        return self.__direction

    def get_radius(self):
        return self.SHIP_RADIUS

    def get_life(self):
        return self.__lives

    def set_direction (self, direction):
        self.__direction = direction

    def set_speed (self, speed):
        self.__speed = speed

    def set_location (self, location):
        self.__location = location

    def reduce_life (self):
        self.__lives -= 1