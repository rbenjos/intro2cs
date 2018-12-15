from car import *
MOVE_POSSIBLE_MESSAGE = 'you can play that car with that movekey'
class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self,cars):
        self.length  = 7
        self.TARGET_CELL = (3.7)
        self.tar_cell_empty = True
        self.cars = cars
        self.current_board = self.get_current_board(cars)
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        pass

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        #The game may assume this function returns a reasonable representation
        #of the board for printing, but may not assume details about it.

        current_board = self.get_current_board(self.cars)
        board_str = ''
        for index, row in enumerate(current_board):
            for cell in row:
                board_str+=cell+' '
            if index == 3:
                board_str+='E\n'
            else:
                board_str+='*\n'
        return board_str


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_list = []
        for y in range (self.length):
            for x in range (self.length):
                cell = (y,x)
                cell_list.append(cell)
        cell_list.append(self.TARGET_CELL)
        return cell_list

        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        pass

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        list_of_valid_moves=[]
        list_of_possible_moves=[]
        for car in self.cars:
            keys = car.possible_moves().keys()
            # print keys
            for movekey in keys:
                cell_required = car.movement_requirements(movekey)
                print(cell_required)
                if self.locations_available(cell_required):
                    list_of_possible_moves.append((car.get_name(),movekey,MOVE_POSSIBLE_MESSAGE))
        return list_of_possible_moves



    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return self.TARGET_CELL

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.cars:
            for car_coor in car.car_coordinates():
                if car_coor == coordinate:
                    return car.get_name()

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if self.locations_available (car.car_coordinates()):
            self.cars.append (car)


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        our_car = None
        for car in self.cars:
            if car.get_name == name:
                our_car = car
                break

        if our_car:
            next_position = our_car.movement_requirements(movekey)
            if self.locations_available (next_position):
                our_car.move(movekey)

    def get_current_board(self, cars):
        current_board = self.get_empty_board()
        for car in self.cars:
            for car_coor in car.car_coordinates():
                current_board[car_coor[0]][car_coor[1]] = car.get_name()
        return current_board


    def get_empty_board(self):
        current_board = []
        for y in range (self.length):
            current_row =[]
            for x in range (self.length):
                current_row.append('_')
            current_board.append(current_row)
        return current_board

    def locations_available (self, coordinates):
        # for car in self.cars:
        #     for car_coor in car.car_coordinates():
        #         for coordinate in coordinates:
        #             if car_coor == coordinate:
        #                 return False
        if coordinates == (3,7):
            return True
        elif coordinates[0] < 0 or coordinates[1] < 0:
            return False
        elif coordinates[0] > 6 or coordinates[1] > 6:
            return False
        if self.cell_content(coordinates)!=None:
            return False
        return True


car1 = Car('R',4,(2,3),1)
car2 = Car('R',4,(0,0),0)


board1=Board([car1,car2])
# print(board1.get_empty_board())
# print(board1.get_current_board([car1,car2]))
print(board1.__str__())
print(board1.possible_moves())