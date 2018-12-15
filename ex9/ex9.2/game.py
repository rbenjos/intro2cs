# Imports
import helper as gh
from car import Car, Direction
from board import Board
from random import randint

# Constants:
WELCOME_MESSAGE = "Welcome to rush Hour game"
RED_CAR_COLOR = "R"
RED_CAR_LENGTH_RANGE = (2, 4)
EXIT_COORDINATE = (3, 0)
CHOOSE_CAR_MESSAGE = "Choose a car you want to move (by color): "
SUCCESS_MESSAGE = "Congratulations! you released the red car!"


# Class definition

class Game:
    """
    A class representing a rush hour game.
    A game is composed of cars that are located on a square board and a user
    which tries to move them in a way that will allow the red car to get out
    through the exit
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        The function runs one round of the game:
        Move car according to user's input. If movement failed (trying to
        move out of board etc.) it returns False, otherwise it returns True.
        """
        color = input(CHOOSE_CAR_MESSAGE)
        if color not in gh.VALID_COLORS:
            print(gh.ERROR_CAR_COLOR)
            return False
        direction = gh.get_direction()
        for car in board.cars:
            if car.color == color:
                if board.move(car, direction):
                    for i in board.__repr__():
                        print(i)
                    return True
        return False

    def play(self):
        """
        The main driver of the Game. Manages the game until completion:
        1. print welcome message
        2. print the board with rhe red car
        3. Get user's input about the cars he wants to add to the board
        4. check if the input is valid. If not it returns to step 3.
        5. print the update board after every car that added.
        6. print succsses message if the user was able to release the red car.

        :return: None
        """

        print(WELCOME_MESSAGE)

        exit_board = board.exit_board
        red_car_location, red_car_orientation = board.get_red_car_parameters()
        red_car = Car(RED_CAR_COLOR, randint(RED_CAR_LENGTH_RANGE[0],
                                             RED_CAR_LENGTH_RANGE[1]),
                      (red_car_location[0] - 1, red_car_location[1] - 1),
                      red_car_orientation)
        if board.add_car(red_car):
            for i in board.__repr__():
                print(i)

        num_cars = gh.get_num_cars()
        for i in range(num_cars):
            color, length, location, orientation = gh.get_car_input(
                self.board.size)
            car = Car(color, length, location, orientation)
            while not board.add_car(car):
                color, length, location, orientation = gh.get_car_input(
                    self.board.size)
                car = Car(color, length, location, orientation)
            for i in board.__repr__():
                print(i)

        while red_car.location != exit_board:
            self.__single_turn()

        if red_car.location == exit_board:
            print(SUCCESS_MESSAGE)

if __name__ == "__main__":
    board = Board([], EXIT_COORDINATE)
    game = Game(board)
    game.play()
