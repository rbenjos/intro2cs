

class Asteroid():

    VALID_SIZE = [1,2,3]

    def __init__ (self,location,speed,size):

        self.__location = location
        self.__speed = speed
        self.__size = size


    def get_speed(self ):
        return self.__speed

    def get_location(self ):
        return self.__location

    def get_size(self ):
        return self.__size

    def get_radius(self):
        radius = (self.get_size()*10-5)
        return radius

    def set_location (self, location):
        self.__location = location

    def has_intersection (self, obj):
        obj_x, obj_y = obj.get_location()[0],obj.get_location()[1]
        ast_x, ast_y = self.get_location()[0],self.get_location()[1]
        ast_r = self.get_radius()
        obj_r = obj.get_radius()
        distance = ((obj_x-ast_x)**2 + (obj_y-ast_y)**2)**0.5

        if distance <= ast_r + obj_r:
            return True
        else:
            return False




