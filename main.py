from generate_new_input import *
from generate_wormholes import *


if __name__ == "__main__":
    print("REPLY CODE CHALLANGE 2023\n")
    DATA = input_data()
    print("\ncreating the file with:", DATA[0], "rows and", DATA[1], "coloumns...\n")
    FILE_ID = generate(DATA)
    print("\ninput_" + FILE_ID + ".txt generated\n")
    with open('raw_inputs/input_' + FILE_ID + '.txt') as f:
        for line in f:
            print(line)
    f.close()
    # CHECKPOINT ACHIEVED: 2 Input format
    print("\ngenerating wormholes...\n")
    generate_wormholes(DATA, FILE_ID)