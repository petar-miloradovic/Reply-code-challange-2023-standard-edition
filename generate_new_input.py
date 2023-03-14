'''
Input file structure:
C(coloumns) R(rows) S(number of snakes)
S values(if s is 5, there will be 5 values here)
{random generated table with R*C}

Input file example:
10 6 5
6 7 5 3 3
1 5 3 6 3 8 5 2 6 8
6 4 * 0 5 3 7 5 2 8
3 4 5 0 3 6 4 * 5 7
3 5 6 3 0 3 5 3 4 6
3 6 7 * 3 0 6 4 5 7
3 7 8 5 3 6 0 4 5 6

Constraints
matrix = {}
C = None # C <= 5000
R = None # R <= 5000
S = None # 1 <= lenght(s) <= 1000
V = None # -10000 <= V <= 10000
'''

import random, uuid

def input_data():
    '''
    function that takes rows, coloumns and the number of snakes as inputs from the user
    return R, C, S as an array
    '''

    # rows number
    R = input("type how many rows you wanna have, the maximum is 5000 rows\n--> ")
    while R.isdigit() == False:
        print("R variable must be an integer")
        R = input("type how many rows you wanna have, the maximum is 5000 rows\n--> ")
    int(R)

    # coloumns number
    C = input("type how many coloumn you wanna have, the maximum is 5000 coloumn\n--> ")
    while C.isdigit() == False:
        print("C variable must be an integer")
        C = input("type how many coloumn you wanna have, the maximum is 5000 coloumn\n--> ")
    int(C)

    # snakes number
    S = input("type how many snakes you wanna have, the maximum is 1000 snakes\n--> ")
    while S.isdigit() == False:
        print("R variable must be an integer")
        S = input("type how many snakes you wanna have, the maximum is 1000 snakes\n--> ")
    int(S)

    # creating the array
    DATA = (R, C, S)

    return DATA

def generate(DATA):
    '''
    create the file with different name each time
    return the file name, R, C and s in a list
    '''

    #taking DATA from input
    R = int(DATA[0])
    C = int(DATA[1])
    S = int(DATA[2])

    # generating the file
    FILE_ID = str(uuid.uuid4())
    input_file_name = "input_" + FILE_ID + ".txt"

    # writing in the file
    with open("raw_inputs/" + input_file_name, 'w') as f:
        f.write(str(C) + " " + str(R) + " " + str(S) + "\n")
        for i in range(0, S, 1):
            f.write(str(random.randint(0, 9)) + " ")
        f.write("\n")
        for i in range(0, C, 1):
            for i in range(0, R, 1):
                f.write(str(random.randint(0, 9)) + " ")  
            f.write("\n")
    f.close()

    return FILE_ID
