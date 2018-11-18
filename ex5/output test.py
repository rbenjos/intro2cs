list_of_tupples = [("hey", 1),("jude", 2),("dont", 3),("make", 4),("it", 4)]

def tupples_to_strings (list_of_tupples):
    list_of_strings = []
    for tupple in list_of_tupples:
        list_of_strings.append(str(tupple))
    return list_of_strings

list_of_strings = tupples_to_strings(list_of_tupples)

f = open('test_output' , 'w')
# f.writelines(list_of_strings)
for tupple in list_of_tupples:
    f.write(str(tupple))
    f.write('\n')
f.close()



print(tupples_to_strings(list_of_tupples))
print(str(list_of_tupples))
print (list_of_tupples)


