import sys
# Open input file for reading and output file for writing
inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w")

def main():
    # Create blank string to store all ASM file instructions
    asmInstructionData = ""

    # Read whole file into the string
    with open(sys.argv[1], "r") as inputFile:
        asmInstructionData = inputFile.read()
        pass

    # Once whole file is read, search for opcode matches

    for i in range(len(asmInstructionData)):

        pass

    pass

if __name__ == '__main__':
    main()
