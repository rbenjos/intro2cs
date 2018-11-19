import random
import string
fi=input('Insert the entry file name(entry.txt): ')
fo=input('Insert the exit file name(.txt): ')
grid_size=[]
words=[]
matrix=[]

def read_file(storage):
    file=open(storage)

    n=file.readline()
    lista=n.split()
    lista=list(map(int,lista))  #sets the size of the grid
    for i in lista:
        grid_size.append(i)

    for line in file:
        line=line.replace("\n","")
        words.append(line)
    file.close()

def grid_generator(grid_size):
    n, p = grid_size
    for i in range(n):
        matriz.append([])
        for j in range(p):
            matriz[i].append(".")

def sets_word_inside(grid_size, word, grid):
    n, p = grid_size
    word = random.choice([word,word[::-1]])
    #horizontal,vertical,diagonal
    d = random.choice([[1,0],[0,1],[1,1]])

    xsize = n  if d[0] == 0 else n  - len(word)
    ysize = p if d[1] == 0 else p - len(word)

    x= random.randrange(0,xsize)
    y= random.randrange(0,ytsize)  #position

    for i, letter in enumerate(word):
        char = grid[y+d[1]*i][x+d[0]*i]
        if char != " " and char != letter:
            # If it reaches an already filled space - restart the            process.
            # The second condition allow the words that cross with repeated words are created.

            return False
        grid[y+d[1]*i][x+d[0]*i] = letter[i]
    return True