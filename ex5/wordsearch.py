# import sys
# import time
#
# word_matrix = []
# with open('matrix_file.txt') as initial_matrix:
#     for line in initial_matrix:
#         word_matrix.append(line.strip().split(','))
#
#
# print(word_matrix)
#
# while(1==1):
#     print (time.time())



def read_wordlist_file(filename):
    list_of_words = list()
    wrd_file = open(filename,'r')
    for line in wrd_file:
        list_of_words.append(line.strip('\n',))
    return list_of_words

list_of_words = read_wordlist_file('word_file.txt')

def read_matrix_file(filename):
    matrix_of_letters = list()
    mtrx_file = open(filename,'r')
    for line in mtrx_file:
        matrix_of_letters.append(line.strip(',\n').split(','))
    return matrix_of_letters

matrix_of_letters = read_matrix_file('matrix_file.txt')

for line in matrix_of_letters:
    print(line,'\n')

print (list_of_words)
directions = ['z']
dictionary_of_words = {}
def find_words_in_matrix (word_list, matrix, directions):
    make_dictionary_of_words()
    tupple_of_pairs = dictionary_to_tupple(dictionary_of_words)
    return tupple_of_pairs


def make_dictionary_of_words():
    for index_y in range(len(matrix_of_letters)):
        for index_x in range(len(matrix_of_letters[0])):
            find_all_words_and_update(index_x,index_y)

def find_all_words_and_update(index_x,index_y):
    for word in list_of_words:
        if matrix_of_letters[index_y][index_x] == word[0]:
            check_word_for_directions(word,index_x,index_y)

def check_word_for_directions(word,index_x,index_y):
    for direction in directions:
        dir_y,dir_x = translate_direction(direction)
        check_word_for_single_direction(word,index_x,index_y,dir_x,dir_y)

def check_word_for_single_direction(word,index_x,index_y,dir_x,dir_y):
        print(matrix_of_letters[index_y][index_x])
        if (check_if_not_out_of_range(word,index_x,index_y,dir_x,dir_y)):
            if(check_if_word_fits(word,index_x,index_y,dir_x,dir_y)):
                update_word_in_dictionary(word)

def update_word_in_dictionary(word):
    if word in dictionary_of_words:
        dictionary_of_words[word] += 1
    else:
        dictionary_of_words[word] =1

def check_if_not_out_of_range(word,index_x,index_y,dir_x,dir_y):
    print("checking if not out of range")
    step_x = dir_x*(len(word))
    step_y = dir_y*(len(word))
    if (((index_x+step_x)>len(matrix_of_letters[0]) or (index_x+step_x)<0)):
        return False
    elif  (((index_y+step_y)>len(matrix_of_letters) or (index_y+step_y)<0)):
        return False
    else:
        return True

def check_if_word_fits(word,index_x,index_y,dir_x,dir_y):
    print("checking if fits")
    created_word = create_word (word,index_x,index_y,dir_x,dir_y)
    if created_word == word:
        return True
    else:
        return False

def create_word(word,index_x,index_y,dir_x,dir_y):
    created_word = ''
    for letter in range(len(word)):
        print(letter*dir_x, letter*dir_y)
        next_letter = matrix_of_letters[index_y+dir_y*letter][index_x+dir_x*letter]
        created_word += next_letter
    print(created_word)
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

make_dictionary_of_words()
print(dictionary_of_words)
        #dictionary of words = {make dictionary of all words found}
        #tupple ={turn dictionary into tupple}:
        #return tupple

#{make dictionary of all words found}
        # #go over line
            # go over letter
                #{update for all words that fit that letter for all directions}



#{update for all words that fit that letter for all directions}:
    #go over words
        # if letter == word[0]:
            #{find word and update for all given directions}

 #{find word and update for all given directions}:

        #for all directions
            #{check and update for single direction}

#{check and update for single direction}:
    #if({check if there is room}):
    #     {check if word is found}:
                # {update dictionary}


#{check if there is room}:

#{check if word is found}:

# {update dictionary}

#}}


#def write_output_file(results, output_filename):
    # {make a text file with python code if needed, empty it if exists}:


    # {open it, write tupple into file when each pair is in a seperate line}:

# {make a text file with python code if needed, empty it if exists}:
    #if (filename exists):
        #empty it
    #else:
        #create filname.txt

# {open it, write tupple into file when each pair is in a seperate line, close it}:
        #open file
        # for every pair:
            #write the pair
            #go down one line
        #close file
