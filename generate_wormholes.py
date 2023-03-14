import random

def generate_wormholes(DATA, FILE_ID):
    R = int(DATA[0])
    C = int(DATA[1])
    S = int(DATA[2])
    input_file_name = "input_" + FILE_ID + ".txt"
    with open('raw_inputs/' + input_file_name, 'r') as f:
        matrix = {}
        i = 0
        count_worm_holes = 0
        worm_holes_number = random.randint(0, S)
        print("there will be", worm_holes_number, "wormholes")
        for lines in f:
            if i > 1:
                line = lines.split(" ")
                line.pop()
                line = list(map(int, line))
                matrix[i] = line
                while count_worm_holes != worm_holes_number:
                    # if random.randint(0, S) == random.randint(0, S):
                    #     matrix[i] = '*'
                        
                    
                # for value in matrix[i]:
                #     
                #         line[random.randint(j)] = '*'
                #         count_worm_holes += 1
                #     if count_worm_holes == S:
                #         break
            i+=1
        print(count_worm_holes)
    print("that's the input file with wormholes generated:\n")
    for line in matrix:
        print(matrix[line])

        f.close()
    print(count_worm_holes)

    return None


