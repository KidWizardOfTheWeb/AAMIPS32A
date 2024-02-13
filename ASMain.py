import sys
import struct

# Open input file for reading and output file for writing
inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "wb") # Make sure we set to "write binary", otherwise it's just text

# Global copy of the whole file, so we can print errors
asmInstructionData = ""

"""
OPCODE FORMAT RULES:
Formatting:
Opcode
reg to store to
reg/imm
reg
dec representation of opcode binary

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
    ('lw', '$r{0:d}', '{1:d}($r{2:d})', 140),
    ('sw', '$r{0:d}', '{1:d}($r{2:d})', 172),
    ('add', '$r{0:d}', '$r{1:d}', '$r{2:d}', 0),
    ('sub', '$r{0:d}', '$r{1:d}', '$r{2:d}', 0),
    ('and', '$r{0:d}', '$r{1:d}', '$r{2:d}', 0),
    ('or', '$r{0:d}', '$r{1:d}', '$r{2:d}', 0),
    ('slt', '$r{0:d}', '$r{1:d}', '$r{2:d}', 0),
    ('beq', '$r{0:d}', '{1:d}', '$r{2:d}', 16),
    ('j', '{0:d}', 8)
]

def validateReg(register):
    if '$' in register:
        # Ensure register is >=0 or <=31
        if int(register.strip('$')) < 0 or int(register.strip('$')) > 31:
            # If not, print the error on the line
            return False
        else:
            return True
    else:
        # Invalid, print error on line
        return False
    pass


def parseInstruction(opcode, params):
    # Input: opcode w/ format, parameters
    # The opcode will be used to reference a format in the libs provided
    # Parameters are passed in and attempt to be written to hex.
    isValidFormat = False
    opcodeToBin = 0
    for i in range(len(opcodeFormats)):
        if opcode == opcodeFormats[i][0]:
            # If parameters are valid, continue.
            isValidFormat = True
            opcodeToBin = opcodeFormats[i][4]
        pass
    if isValidFormat is False:
        # If parameters are not valid, print which line in the input file throws an error
        return

    # Create a bytearray, so we can write binary to the file

    for i in range(3):
        if i is 0:
            if not validateReg(params[0]):
                return
            else:
                pass
        else:
            if '$' in params[i]:
                # Ensure register is >=0 or <=31
                if not params[i].strip('$').isdigit():

                    # If not, print the error on the line
                    return
                else:
                    # Continue if valid
                    pass
            else:
                # Invalid, print error on line
                pass
        pass

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
        paramsArray = params.strip().split(',')
        paramsArray[0] = paramsArray[0].strip(" ")
        paramsArray[1] = paramsArray[1].strip(" ")
        paramsArray[2] = paramsArray[2].strip(" ")
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
                parseInstruction(opcodeID, paramsArray)
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
        if mutableData.find('\n') is not -1:
            # Increment to next line here
            mutableData = mutableData[mutableData.find('\n') + 1:]
        else:
            # End the loop here
            break
        pass

    pass


if __name__ == '__main__':
    main()
