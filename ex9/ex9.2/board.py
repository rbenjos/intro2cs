# Imports:
import helper as gh
from car import Car, Direction

# Constants:
VERTICAL = 0
HORIZONTAL = 1
ERROR_NOT_EMPTY = 'Place is not available. Please try again.'
BOARD_SIZE = 6
NOT_VALID_EXIT = 'Exit is not valid'
EXIT = 'E'
MIN_CAR_LENGTH = 2
MAX_CAR_LENGTH = 4
EDGE = '-'
FREE_SPACE = '_'


class Board:
    """
    A class representing a rush hour board.
    """

    def __init__(self, cars, exit_board, size=6):
        """
        Initialize a new Board object.
        :param cars: A list of cars.
        :param size: Size of board (Default size is 6).
        """
        self.cars = cars
        self.exit_board = exit_board
        self.size = size

    def add_exit_to_board(self):
        """
        Add a sign that representing the exit to the board.
        """
        board = self.BoardGame
        exit_board = self.exit_board

        if exit_board[0] == len(board) - 3:
            board[exit_board[0] + 2][exit_board[1] + 1] = EXIT
        if exit_board[0] == 0:
            board[exit_board[0]][exit_board[1] + 1] = EXIT
        if self.exit_board[1] == 5:
            board[exit_board[0] + 1][exit_board[1] + 2] = EXIT
        if exit_board[1] == 0:
            board[exit_board[0] + 1][exit_board[1]] = EXIT

    def get_red_car_parameters(self):
        """
        Adjust the values of the red car to the value of the board exit.
        :return: tuple of adjusted red car location and
        adjusted red car orientation.
        """
        exit_board = self.exit_board
        if exit_board[0] == 0:
            red_car_location = exit_board[0] + 3, exit_board[1] + 1
            red_car_orientation = VERTICAL
            return red_car_location, red_car_orientation
        if exit_board[0] == self.size:
            red_car_location = exit_board[0] - 3, exit_board[1] + 1
            red_car_orientation = VERTICAL
            return red_car_location, red_car_orientation
        if exit_board[1] == 0:
            red_car_location = exit_board[0] + 1, exit_board[1] + 3
            red_car_orientation = HORIZONTAL
            return red_car_location, red_car_orientation
        if exit_board[1] == self.size:
            red_car_location = exit_board[0] + 1, exit_board[1] - 3
            red_car_orientation = HORIZONTAL
            return red_car_location, red_car_orientation

    def add_car(self, car):
        """Add a single car to the board.
        :param car: A car object
        :return: True if a car was successfully added, or False otherwise."""

        # check if the color is valid
        invalid_colors = []
        for car_item in self.cars:
            invalid_colors.append(car_item.color)
        if car.color in invalid_colors or car.color not in gh.VALID_COLORS:
            print(gh.ERROR_CAR_COLOR)
            return False

        # check if the length is valid
        if not MIN_CAR_LENGTH <= car.length <= MAX_CAR_LENGTH:
            print(gh.ERROR_CAR_LEN)
            return False

        # check if the place is free
        if not self.is_empty(car.location):
            return False
        if car.orientation == VERTICAL:
            row = car.location[0] + car.length - 1
            if row >= self.size:
                print(gh.ERROR_COORDINATE_OUT_OF_BOUND + str(self.size))
                return False
        if car.orientation == HORIZONTAL:
            column = car.location[1] + car.length - 1
            if column >= self.size:
                print(gh.ERROR_COORDINATE_OUT_OF_BOUND + str(self.size))
                return False

        # check if the orientation is valid
        if car.orientation != HORIZONTAL and car.orientation != VERTICAL:
            print(gh.ERROR_CAR_ORN)
            return False

        self.cars.append(car)
        return True

    def is_empty(self, location):
        """
        Check if a given location on the board is free.
        :param location: x and y coordinates of location to be check
        :return: True if location is free, False otherwise
        """

        if not 0 <= location[0] < self.size or not 0 <= location[
            1] < self.size:
            print(gh.ERROR_COORDINATE_OUT_OF_BOUND + str(self.size - 1))
            return False

        for car in self.cars:
            if car.orientation == HORIZONTAL:
                for i in range(car.length):
                    if location == (car.location[0], car.location[1] + i):
                        print(ERROR_NOT_EMPTY)
                        return False

            if car.orientation == VERTICAL:
                for i in range(car.length):
                    if location == (car.location[0] + i, car.location[1]):
                        print(ERROR_NOT_EMPTY)
                        return False

        return True

    def move(self, car, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False
            otherwise.
            """

        if car.orientation == VERTICAL:
            if direction == Direction.UP:
                cur_location = car.location[0] - 1, car.location[1]
                if self.is_empty(cur_location):
                    car.location = cur_location
                    return True
                else:
                    return False

            elif direction == Direction.DOWN:
                cur_location = car.location[0] + car.length, car.location[1]
                if self.is_empty(cur_location):
                    car.location = car.location[0] + 1, car.location[1]
                    return True
                else:
                    return False
            else:
                print(gh.ERROR_DIRECTION)
                return False

        if car.orientation == HORIZONTAL:
            if direction == Direction.RIGHT:
                cur_location = car.location[0], car.location[1] + car.length
                if self.is_empty(cur_location):
                    car.location = car.location[0], car.location[1] + 1
                    return True
                else:
                    return False

            elif direction == Direction.LEFT:
                cur_location = car.location[0], car.location[1] - 1
                if self.is_empty(cur_location):
                    car.location = cur_location
                    return True
                else:
                    return False
            else:
                print(gh.ERROR_DIRECTION)
                return False

    def __repr__(self):
        """
        :return: Return a string representation of the board.
        """
        self.BoardGame = []

        # built the board
        first_row = []
        first_row.append(EDGE)
        for i in range(self.size):
            first_row.append(str(i))
        first_row.append(EDGE)
        self.BoardGame.append(first_row)

        for i in range(self.size):
            row = []
            row.append(str(i))
            for j in range(self.size):
                row.append(FREE_SPACE)
            row.append(str(i))
            self.BoardGame.append(row)

        last_row = []
        last_row.append(EDGE)
        for i in range(0, self.size):
            last_row.append(str(i))
        last_row.append(EDGE)
        self.BoardGame.append(last_row)

        self.add_exit_to_board()

        # update the board with the cars
        for car in self.cars:
            car_real_location = (car.location[0] + 1, car.location[1] + 1)
            if car.orientation == HORIZONTAL:
                for i in range(car_real_location[1],
                               car_real_location[1] + car.length):
                    if self.BoardGame[car_real_location[0]][i] != FREE_SPACE:
                        print(ERROR_NOT_EMPTY)
                        return FREE_SPACE
                    self.BoardGame[car_real_location[0]][i] = car.color

            if car.orientation == VERTICAL:
                for i in range(car_real_location[0], car_real_location[0] +
                        car.length):
                    if self.BoardGame[i][car_real_location[1]] != FREE_SPACE:
                        print(ERROR_NOT_EMPTY)
                        return FREE_SPACE
                    self.BoardGame[i][car_real_location[1]] = car.color

        return self.BoardGame
