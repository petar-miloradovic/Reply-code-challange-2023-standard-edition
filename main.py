from generate_new_input import *
from generate_wormholes import *


if __name__ == "__main__":
    print("REPLY CODE CHALLANGE 2023\n")
    data = input_data()
    print("\ncreating the file with:", data[0], "rows and", data[1], "coloumns...\n")
    FILE_ID = generate(data)
    print("\ninput_" + FILE_ID + ".txt generated\n")
    # CHECKPOINT ACHIEVED: 2 Input format
    generate_wormholes(data)