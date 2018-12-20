
class Torpedo ():

    TORPEDO_RADIUS = 4

    def __init__(self, location, speed, direction):
        self.__location = location
        self.__speed = speed
        self.__direction = direction
        self.__age = 0


    def get_speed(self ):
        return self.__speed

    def get_location(self ):
        return self.__location

    def get_direction(self ):
        return self.__direction

    def get_radius(self):
        return self.TORPEDO_RADIUS

    def get_age(self):
        return self.__age

    def set_location(self, location):
        self.__location = location

    def set_age(self,age):
        self.__age = age
