

import sys
import os.path
import random

from typing import List, Any

ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
VALID_LENGTH_OF_ARGS = 4
VALID_DIRECTION = 'rludwxyz'

args = [sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]



############################### supplementary code for testing ##########################

# takes the randomised matrix and turn it into a text file, which is good for the final testing
def write_matrix_file(matrix_with_letters):
    output_file = open('matrix_for_test.txt','w')
    for line in matrix_with_letters:
        for index_letter in range(len(line)):
            output_file.write(str(line[index_letter]))
            if (index_letter != len(line)-1):
                output_file.write(',')
        output_file.write('\n')
    output_file.close()

# takes a solved matrix of letters and add random letters instead of '_' so we can get a proper wordsearch
def randomise_letters(solved_matrix_of_letters):
    for y in range(len(solved_matrix_of_letters)):
        for x in range(len(solved_matrix_of_letters[0])):
            if (solved_matrix_of_letters[y][x] == '_'):
                solved_matrix_of_letters[y][x] = random.choice(ALPHABET)
    return solved_matrix_of_letters




############################### supplementary code for testing ##########################

# the function checks for the validity of all the inputs
def check_input_args(args):
    if ((len(args)-1) != VALID_LENGTH_OF_ARGS): #it checks if there's the right number of inputs
        print("the number of arguments is not valid")
    if(not (set(args[4])<=set((VALID_DIRECTION)))): # if the directions given were valid
        print("the direction given isn't valid")
    if (not os.path.isfile(args[1])):  # and if the input files exist
        print ("file of list of words doesn't extist")
    if (not os.path.isfile(args[2])):
        print ("file of matrix of letters doesn't exist")
    else:
        return None # if all is well, it returns 'None'


# the function takes the name of the file of the list of words and returns a list of words in python
def read_wordlist_file(filename):
    word_list  = list() # first we make a new list
    wrd_file = open(filename,'r')
    for line in wrd_file:         # we open the document and we append every word to the list without the '\n' character
        word_list.append(line.strip('\n'))
    return word_list


# the function takes the name of the file of the matrix of letters and returns a list of list which represents the matrix
def read_matrix_file(filename):
    matrix_of_letters = list()  # we make a new list
    mtrx_file = open(filename,'r')
    for line in mtrx_file: # open the file, and append every line to the list, while splitting every line to a list by itself
        matrix_of_letters.append(line.strip('\n').split(','))
    return matrix_of_letters #thus getting a list of lists



def find_words_in_matrix (word_list, matrix, directions):
    dictionary_of_words ={}
    dictionary_of_words = make_dictionary_of_words(word_list,matrix,directions,dictionary_of_words)
    list_of_tupples = dictionary_to_tupples(dictionary_of_words)
    return list_of_tupples

def dictionary_to_tupples (dictionary_of_words):
    list_of_tupples = dictionary_of_words.items()
    return list_of_tupples


def make_dictionary_of_words(word_list,matrix,directions,dictionary_of_words):
    for index_y in range(len(matrix)):
        for index_x in range(len(matrix[0])):
            dictionary_of_words = check_for_all_words_and_update(word_list,matrix,directions,dictionary_of_words,index_x,index_y)
    return dictionary_of_words

def check_for_all_words_and_update(word_list,matrix,directions,dictionary_of_words,index_x,index_y):
    for word in word_list:
        if LETTER_MATRIX[index_y][index_x] == word[0]:
            dictionary_of_words =check_word_for_directions(matrix,directions,dictionary_of_words,word,index_x,index_y)
    return dictionary_of_words

def check_word_for_directions(matrix,directions,dictionary_of_words,word,index_x,index_y):
    for direction in directions:
        dir_y,dir_x = translate_direction(direction)
        dictionary_of_words = check_word_for_single_direction(matrix,directions,dictionary_of_words,word,index_x,index_y,dir_x,dir_y)
    return dictionary_of_words

def check_word_for_single_direction(matrix,directions,dictionary_of_words,word,index_x,index_y,dir_x,dir_y):
    if (check_if_not_out_of_range(word,index_x,index_y,dir_x,dir_y)):
        if(check_if_word_fits(word,index_x,index_y,dir_x,dir_y)):
            dictionary_of_words = update_word_in_dictionary(dictionary_of_words,word)
    return dictionary_of_words

def update_word_in_dictionary(dictionary_of_words,word):
    if word in dictionary_of_words:
        dictionary_of_words[word] += 1
    else:
        dictionary_of_words[word] =1
    return dictionary_of_words

def check_if_not_out_of_range(word,index_x,index_y,dir_x,dir_y):
    step_x = dir_x*(len(word))
    step_y = dir_y*(len(word))
    if (((index_x+step_x) > len(LETTER_MATRIX[0]) or (index_x + step_x) < 0)):
        return False
    elif  (((index_y+step_y) > len(LETTER_MATRIX) or (index_y + step_y) < 0)):
        return False
    else:
        return True

def check_if_word_fits(word,index_x,index_y,dir_x,dir_y):
    created_word = create_word (word,index_x,index_y,dir_x,dir_y)
    if created_word == word:
        return True
    else:
        return False

def create_word(word,index_x,index_y,dir_x,dir_y):
    created_word = ''
    for letter in range(len(word)):
        next_letter = LETTER_MATRIX[index_y + dir_y * letter][index_x + dir_x * letter]
        created_word += next_letter
    return created_word

def translate_direction(direction):
    if direction == 'r':
        return 0,1
    elif direction == 'l':
        return 0,-1
    elif direction == 'u':
        return -1,0
    elif direction == 'd':
        return 1,0
    elif direction =='w':
        return -1,1
    elif direction =='x':
        return -1,-1
    elif direction =='y':
        return 1,1
    elif direction=='z':
        return 1,-1


def write_output_file(results, output_filename):
    output_file = open(output_filename, 'w')
    # f.writelines(list_of_strings)
    for tupple in results:
        string_of_tupple = str(tupple)
        stripped_string = string_of_tupple.strip('(')
        stripped_string =stripped_string.strip(')')
        output_file.write(stripped_string)
        output_file.write('\n')
    output_file.close()


def play_wordsearch(args):
    # if not (check_input_args(args)):
        word_list = read_wordlist_file(args[1])
        LETTER_MATRIX = read_matrix_file(args[2])
        # directions = set(args[4])
        directions = 'rludwxyz'

        results = find_words_in_matrix(word_list,LETTER_MATRIX,directions)
        write_output_file(results,args[3])


LETTER_MATRIX = read_matrix_file(args[2])
WORD_LIST = read_wordlist_file(args[1])
# DIRECTIONS = set(args[4])
DIRECTIONS = 'rlduwxyz'
play_wordsearch(args)

results = find_words_in_matrix(WORD_LIST,LETTER_MATRIX,DIRECTIONS)

#################### displaying the outputs of the code ################

print('\n')
print(args)
print('\n')

for line in LETTER_MATRIX:
    print(line)


matrix_with_randoms = randomise_letters(LETTER_MATRIX)
write_matrix_file(matrix_with_randoms)

print('\n')

for line in LETTER_MATRIX:
    print(line)

print('\n')

print (WORD_LIST)
print('\n')

write_output_file(results,'output_test.txt')


print(results)

print('\n')
print('the output would look like this:')
print('\n')

for tupple in results:
    string_of_tupple = str(tupple)
    stripped_string = string_of_tupple.strip('(')
    stripped_string =stripped_string.strip(')')
    print(stripped_string)
#################### displaying the outputs of the code ################