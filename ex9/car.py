

class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):

        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"

    def car_coordinates(self):

        list_of_coordinates = []
        if self.orientation == 0:
            for y in range (self.length):
                coordinate = [self.location[0]+y,self.location[1]]
                list_of_coordinates.append(coordinate)


        if self.orientation == 1:
            for x in range (self.length):
                coordinate = [self.location[0],self.location[1]+x]
                list_of_coordinates.append(coordinate)

        return list_of_coordinates

        # implement your code and erase the "pass"


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        ud_moves = {'u': 'makes the car go up',
                    'd': 'makes the car go down'}

        rl_moves = {'r': 'makes the car go right',
                    'l': 'makes the car go left'}

        if self.orientation == 0:
            return ud_moves
        elif self.orientation == 1:
            return rl_moves
        #For this car type, keys are from 'udrl'
        #The keys for vertical cars are 'u' and 'd'.
        #The keys for horizontal cars are 'l' and 'r'.
        #You may choose appropriate strings.
        # implement your code and erase the "pass"
        #The dictionary returned should look something like this:
        #result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        #A car returning this dictionary supports the commands 'f','d','a'.


    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        if movekey == 'u':
            return [self.location[0]-1,self.location[1]]

        elif movekey == 'd':
            return [self.location[0]+1+self.length,self.location[1]]

        elif movekey == 'r':
            return [self.location[0],self.location[1]+1+self.length]

        elif movekey == 'l':
            return [self.location[0],self.location[1]-1]

        #For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        #be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"


    def move(self, movekey):
        if self.orientation == 0:
            if movekey == 'u':
                self.location[0] -= 1
                return True
            elif movekey == 'd':
                self.location[0] += 1
                return True
        elif self.orientation == 1:

            if movekey == 'r':
                self.location[1] += 1
                return True
            elif movekey == 'l':
                self.location[1] -= 1
                return True

        else:
            return False



    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name
        # implement your code and erase the "pass"


