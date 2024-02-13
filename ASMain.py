import sys
import struct

# Open input file for reading and output file for writing
inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w")

"""
OPCODE FORMAT RULES:
1. Check opcode by reading first index of tuple.
2. If valid, fill parameters into tuple.
3. Return this. If the parameters are the wrong length, return error.
3a. EX. 
and $5, $6, $40 IS NOT VALID
3b. The storage regs (first param) will be 0-31. Accepted reg types are r currently.
3c. The second param (either an immediate or register) depends. If immediate, there is no int limit. If register,
follow above step.
3d. The third param (if it exists) will be a register. If a jump-involved opcode, it is an immediate.
"""

opcodeFormats = [
    ('lw', '$r{0:d}', '{1:d}($r{2:d})'),
    ('sw', '$r{0:d}', '{1:d}($r{2:d})'),
    ('add', '$r{0:d}', '$r{1:d}', '$r{2:d}'),
    ('sub', '$r{0:d}', '$r{1:d}', '$r{2:d}'),
    ('and', '$r{0:d}', '$r{1:d}', '$r{2:d}'),
    ('or', '$r{0:d}', '$r{1:d}', '$r{2:d}'),
    ('slt', '$r{0:d}', '$r{1:d}', '$r{2:d}'),
    ('beq', '$r{0:d}', '{1:d}', '$r{2:d}'),
    ('j', '{0:d}')
]
# opcodeFormats = [
#     ("lw", "$r%d", "%d($r%d)"),
#     ("sw", "$r%d", "%d($r%d)"),
#     ("add", "$r%d", "$r%d"),
#     ("sub", "$r%d", "$r%d"),
#     ("and", "$r%d", "$r%d"),
#     ("or", "$r%d", "$r%d"),
#     ("slt", "$r%d", "$r%d"),
#     ("beq", "$r%d", "%d"),
#     ("j", "%d"),
# ]

def parseInstruction(opcode, params):
    # Input: opcode w/ format, parameters
    # The opcode will be used to reference a format in the libs provided
    # Parameters are passed in and attempt to be written to hex.
    # If parameters are valid, write to output file.
    # If parameters are not valid, print which line in the input file throws an error
    for i in range (len(opcodeFormats)):
        if opcode == opcodeFormats[i][0]:
            pass
        pass
    # match opcode:
    #     case num:
    #         pass
    #     case _:
    #         pass
    pass


def main():
    # Create blank string to store all ASM file instructions
    asmInstructionData = ""

    # Read whole file into the string
    with open(sys.argv[1], "r") as inputFile:
        asmInstructionData = inputFile.read()
        pass

    # Once whole file is read, search for opcode matches

    mutableData = asmInstructionData
    for i in range(len(asmInstructionData)):
        # Opcode matches are found here with a match-case.
        # Once a match is found, calls parseInstruction
        # parseInstruction will have an opcode format passed in, as well as the parameters from the input file
        opcodeID = mutableData.partition(" ")[0]  # partition returns 3 items. Find the opcode before the space.
        params = mutableData.partition("\n")[0]  # partition returns 3 items. Find the opcode before the space.
        params = params.partition(" ")[2]
        # after we find the opcode, find if second param is imm or reg
        # we can do this by finding mutableData.partition(" ")[2] (everything after the first space), then running
        # partition("$")[2] again to find the next param.
        # If we find x after, it's an imm.
        # If we find rx after, it's a reg.
        # pass the params and param amount into the parseInstruction func after
        match opcodeID:
            case 'lw':
                pass
            case 'sw':
                pass
            case 'add':
                # this should pass in:
                # param 1 = the opcode
                # param 2 = all params
                # print("got in")
                parseInstruction(opcodeID, params)
                pass
            case 'sub':
                pass
            case 'and':
                pass
            case 'or':
                pass
            case 'slt':
                pass
            case 'beq':
                pass
            case 'j':
                pass
            case _:
                pass
        pass

    pass


if __name__ == '__main__':
    main()
