import json
from helper import *
from board import *
from car import *

class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board
        #You may assume board follows the API
        # implement your code here (and then delete the next line - 'pass')
        self.board = board
    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        # implement your code here (and then delete the next line - 'pass')
        self.single_turn_input = input(SINGLE_TURN_MESSAGE)
        input_name, input_direction = self.single_turn_input.split(',')
        if turn_input_valid(input_name,input_direction):
            self.board.move_car(input_name,input_direction)
        else:
            print (INVALID_TURN_INPUT_MESSAGE)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code here (and then delete the next line - 'pass')
        while not self.board.tar_cell_empty:
            self.__single_turn()

if __name__== "__main__":
    #Your code here
    #All access to files, non API constructors, and such must be in this
    #section, or in functions called from this section.
    json_path = input(JASON_INPUT_MESSAGE)
    cars_on_board = load_json(json_path)
    board_for_game = Board(cars_on_board)
    current_game = Game(board_for_game)
