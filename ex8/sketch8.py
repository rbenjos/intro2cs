import random
import time
import copy

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def solve_sudoku(board):


def solve_sudoku_helper(board,posx,posy):
    n_posy,n_posx = next_pos(board,posx,posy)
    # if board_full(board):
    if n_posy == -1:
        print_board(board)
        print('this is a solution')
        return True

    if board[posy][posx] == 0:
        for num in range (1,10):
            if can_be_placed(num,board,posy,posx):
                board[posy][posx] = num
                # print('')
                # print_board(board)
                # print('')
                if solve_sudoku_helper(board,n_posx,n_posy):
                    return True
                board[posy][posx] = 0
    elif solve_sudoku_helper(board,n_posx,n_posy):
        return True
    return False




def next_pos(board,posy,posx):
    for x in range (posy, len(board)):
        for y in range (posx,len(board)):
            if board[x][y] == 0:
                return x,y

    for x in range (0, len(board)):
        for y in range (0,len(board)):
            if board[x][y] == 0:
                return x,y

    return -1,-1

    # if board[posy][posx] == 0:
    #     for num in range (1,10):
    #         if can_be_placed(num,board,posy,posx):
    #             board[posy][posx] = num
    #             if posx < len(board)-1:
    #                 print_board(board)
    #                 solve_sudoku_helper(board,posx+1,posy)
    #             elif posy < len(board)-1:
    #                 print_board(board)
    #                 solve_sudoku_helper(board,0,posy+1)
    #             else:
    #                 if posx < len(board)-1:
    #                     print_board(board)
    #                     solve_sudoku_helper(board,posx+1,posy)
    #                 elif posy < len(board)-1:
    #                     print_board(board)
    #                     solve_sudoku_helper(board,0,posy+1)
    #                 else:
    #                     board[posy][posx]=0
    #                     return
    #


# for i in range(len(board)):
#     for j in range(len(board)):
#         if board[i][j] == 0:
#             for num in range(1, 10):
#                 if (can_be_placed(num,board,i,j)):
#                     board[i][j] = num
#                     print('')
#                     print_board(board)
#                     print(time.clock())
#                     if not (solve_sudoku_helper(board)):
#                         print('dead end')

def board_full(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return False
    return True

def print_board(board):
    for row in range(len(board)):
        print board[row]

def can_be_placed(num,board,i,j):
    return (not_in_row(num, board, i) and
            not_in_col(num, board, j) and
            not_in_block(num, board, i,j))

def not_in_row(num, board, i):
    for index in range(len(board)):
        if board[i][index] == num:
            return False
    return True


def not_in_col(num, board, j):
    for index in range(len(board)):
        if board[index][j] == num:
            return False
    return True


def not_in_block(num, board, i, j):
    block_len = int(len(board) ** 0.5)
    block_row_start = find_start(i, block_len)
    block_col_start = find_start(j, block_len)

    for row in range(block_row_start, block_row_start + block_len):
        for col in range(block_col_start, block_col_start + block_len):
            if num == board[row][col]:
                return False
    return True


def find_start(index, block_length):
    start = 0
    while (start + block_length <= index):
        start += block_length
    return start


first_board = [[4, 8, 7, 7, 1, 4, 3, 9, 2],
               [3, 2, 8, 4, 7, 2, 2, 4, 4],
               [2, 3, 9, 1, 1, 5, 5, 5, 1],
               [2, 8, 9, 6, 4, 5, 6, 5, 9],
               [3, 6, 7, 8, 5, 1, 1, 5, 6],
               [6, 2, 9, 6, 6, 5, 3, 6, 7],
               [6, 5, 9, 7, 8, 3, 2, 1, 2],
               [5, 1, 4, 8, 8, 2, 2, 8, 3],
               [7, 6, 2, 9, 3, 9, 5, 4, 9]]

solved_example = [[7,3,5,6,1,4,8,9,2],
                  [8,4,2,9,7,3,5,6,1],
                  [9,6,1,2,8,5,3,7,4],
                  [2,8,6,3,4,9,1,5,7],
                  [4,1,3,8,5,7,9,2,6],
                  [5,7,9,1,2,6,4,3,8],
                  [1,5,7,4,9,2,6,8,3],
                  [6,9,4,7,3,8,2,1,5],
                  [3,2,8,5,6,1,7,4,9]]



solved_example_missing_2 = [[7,3,5,6,1,4,8,0,0],
                            [8,4,2,9,7,3,5,6,1],
                            [9,6,1,2,8,5,3,7,4],
                            [0,8,6,3,4,9,1,5,7],
                            [4,1,3,8,5,7,9,0,6],
                            [5,7,9,1,2,6,4,3,8],
                            [1,5,7,4,9,2,6,8,3],
                            [6,9,4,7,3,8,0,1,5],
                            [3,2,8,5,6,1,7,4,9]]



solved_example_missing_few = [[0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,5,3,0,0],
                              [0,0,6,3,0,9,0,0,0],
                              [4,0,0,0,0,7,9,0,0],
                              [5,7,0,1,0,6,4,0,0],
                              [1,5,0,4,0,2,6,8,0],
                              [6,9,4,7,0,8,0,1,0],
                              [3,2,8,5,6,1,0,4,0]]

#
# for i in range(9):
#     row = []
#     for j in range(9):
#         number= random.choice(DIGITS)
#         row.append(number)
#     print(row)
#
# print (not_in_row(9,first_board,0))
# print (not_in_col(9,first_board,0))

solve_sudoku_helper(solved_example_missing_few,0,0)

