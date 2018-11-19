
#################################################### for the test################################3


def read_wrdlst_tst(filename):

    list_of_words = list()
    wrd_file = open(filename,'r')
    for line in wrd_file:
        list_of_words.append(line.strip('\n',))
    return list_of_words



def read_mat_tst(filename):

    matrix_of_letters = list()
    mtrx_file = open(filename,'r')
    for line in mtrx_file:
        matrix_of_letters.append(line.strip('\n').split(' '))
    return matrix_of_letters

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

wrd_lst_test = read_wrdlst_tst('test_word_list.txt')

mat_test = read_mat_tst('test_mat.txt')

for element in mat_test:
    if (not str(element) in ALPHABET):
        mat_test.remove(element)


print (mat_test)
#################################################### for the test################################3
