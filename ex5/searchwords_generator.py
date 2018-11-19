import random
from copy import deepcopy
def make(row,column):
    return [['_' for _ in range(column)] for a in range(row)] # Generates a empty array of specified width(column) and height(row)
def add_horizontally(word,array,row,column,backwards=False):
    arr = deepcopy(array) #Copy the array because we may make unwanted mutations
    word = word[::-1] if backwards else word #If backwards is true reverse the word
    somearr = list(word)
    for c in somearr:
        if((arr[row][column] != '_') & (arr[row][column] != c)): #If there already exists a character and it is not same as c then
            raise Exception("Oh the letter is already there") #Throw a error
        else:
            arr[row][column] = c #Else add the letter to the correct row and column
            column += 1 #Increase column by 1
    return arr
def add_vertically(word,array,row,column,backwards=False): #Same as add horizontally except it increases row by 1
    arr = deepcopy(array)
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if((arr[row][column] != '_') &  (arr[row][column] != c)):
            raise Exception("Oh the letter is already there")
        else:
            arr[row][column] = c
            row += 1
    return arr
def add_diagonally(word,array,row,column,backwards=False): #Same as add_vertically except increase both row and cloumn by 1
    arr = deepcopy(array)
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if((arr[row][column] != '_') & (arr[row][column] != c)):
            raise Exception("Oh the letter is already there")
        else:
            arr[row][column] = c
            row += 1
            column += 1
    return arr
def random_condition(rows,columns,backwards=True,diagonals=True): # Generate a random condition for the placement of word
    row = random.randint(0,rows)
    column = random.randint(0,columns)
    backward = backwards if not backwards else [True,False][random.randint(0,1)] #If backwards is false let it remain so else generate a random value
    diagonal = diagonals if not diagonals else [True,False][random.randint(0,1)] #Same as above
    return (row,column,backward,diagonal)
def check(condition,word): # Check ifthe provided condition is fitting i.e. there should be no out of index problem
    diagonal = condition[0][3]
    row_start = condition[0][0]
    column_start = condition[0][1]
    rows = condition[1]
    columns = condition[2]
    vertical = condition[3]
    if(diagonal):
        if(((rows-row_start) >= len(word)) & ((columns - column_start) >= len(word))):
            return True
        else:
            return False
    if(vertical):
        if(rows-row_start>len(word)):
            return True
        else:
            return False
    else:
        if(columns - column_start>len(word)):
            return True
        else:
            return False
def random_alpha(): # Returns a random alphabet
    return 'abcdefghijklmnopqrstuvwxyz'[random.randint(0,25)]
def randomize(arr): # After the grid is made fill the remaining places with randome characters
    return [[m if m!='_' else random_alpha() for m in a] for a in arr]
def generate(row,column,word_list,backwards=True,diagonal=True): # Uses all the above methods to make array
    if((max(len(w) for w in word_list) > row) | (max(len(w) for w in word_list) > column)): #If the word is larger than row or column length than return 'wrong'.
        return ('wrong',)
    else:
        pass
    array = make(row,column)
    row -= 1 # Because indexing starts at 0!
    column -= 1 # Because indexing starts at 0!!
    for word in word_list:
        i = True
        while(i):
            vertical = False
            conditions = random_condition(row,column,backwards=backwards,diagonals=diagonal)
            if(not conditions[3]): # If diagonal is false
                vertical = [True,False][random.randint(0,1)]
            if (check((conditions,row,column,vertical),word)):
                if(conditions[3]): # If diagonal is true
                    try: # We may throw a error
                        array = deepcopy(add_diagonally(word,array,conditions[0],conditions[1],conditions[2]))
                        i = False
                    except Exception:
                        pass
                elif(vertical):
                    try:
                        array = deepcopy(add_vertically(word,array,conditions[0],conditions[1],conditions[2]))
                        i = False
                    except Exception:
                        pass
                else :
                    try:
                        array = deepcopy(add_horizontally(word,array,conditions[0],conditions[1],conditions[2]))
                        i = False
                    except Exception:
                        pass
    return randomize(array) # Fill with random characters
def text(arr): # Convert given array to text
    str = ''
    for row in arr:
        for word in row:
            str += word + ' '
        str += '\n'
    return str
open('test.txt','w').write(text(generate(15,15,['Lord','Voldemort','likes','penpineapple','applepen']))) # To test it!