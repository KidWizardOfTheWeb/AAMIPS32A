import sys
from struct import pack, unpack

# Open input file for reading and output file for writing
inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "wb") # Make sure we set to "write binary", otherwise it's just text

# Global copy of the whole file, so we can print errors
asmInstructionData = ""

"""
OPCODE FORMAT RULES:
Formatting:
Opcode ID
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

# Includes ordering for params
opcodeData = [
    ('lw', 2, 0, 1),
    ('sw', 2, 0, 1),
    ('add', 1, 2, 0),
    ('sub', 1, 2, 0),
    ('and', 1, 2, 0),
    ('or', 1, 2, 0),
    ('slt', 1, 2, 0),
    ('beq', 0, 1, 2),
    ('j', 1, 0)
]
#('add', bin(int('000000', 2)), '{1:05b}', '{2:05b}', '{0:05b}', bin(int('00000', 2)), bin(int('100000', 2))),
opcodeFormats = [
    ('lw', bin(int('100011', 2)), '{0:05b}', '{0:05b}', '{0:016b}'),
    ('sw', bin(int('101011', 2)), '{0:05b}', '{0:05b}', '{0:016b}'),
    ('add', '{0:05b}'.format(0), '{0:05b}', '{0:06b}', '{0:05b}', 0, 32),
    ('sub', '{0:05b}'.format(0), '{0:05b}', '{0:06b}', '{0:05b}', 0, 34),
    ('and', '{0:05b}'.format(0), '{0:05b}', '{0:06b}', '{0:05b}', 0, 36),
    ('or', '{0:05b}'.format(0), '{0:05b}', '{0:06b}', '{0:05b}', 0, 37),
    ('slt', '{0:05b}'.format(0), '{0:05b}', '{0:06b}', '{0:05b}', 0, 42),
    ('beq', '{0:06b}'.format(4), '{0:05b}', '{0:05b}', '{0:016b}'),
    ('j', bin(int('000010', 2)), '{0:026b}')
]

# opcodeFormats = [
#     ('lw', '$r{0:d}', '{1:d}($r{2:d})', bin(0x23)),
#     ('sw', '$r{0:d}', '{1:d}($r{2:d})', bin(0x2B)),
#     ('add', '$r{0:d}', '$r{1:d}', '$r{2:d}', bin(0x20)),
#     ('sub', '$r{0:d}', '$r{1:d}', '$r{2:d}', bin(0x22)),
#     ('and', '$r{0:d}', '$r{1:d}', '$r{2:d}', bin(0x24)),
#     ('or', '$r{0:d}', '$r{1:d}', '$r{2:d}', bin(0x25)),
#     ('slt', '$r{0:d}', '$r{1:d}', '$r{2:d}', bin(0x2A)),
#     ('beq', '$r{0:d}', '{1:d}', '$r{2:d}', bin(0x4)),
#     ('j', '{0:d}', bin(0x2))
# ]


def validateReg(register, storageFlag):
    if storageFlag == 0 and '$' not in register:
        # Ensure first param is a register
        return False
    if '$' in register:
        # Ensure register is >=0 or <=31
        if int(register.strip('$')) < 0 or int(register.strip('$')) > 31:
            # If not, print the error on the line
            return False
        else:
            return True
    else:
        # Invalid, print error on line
        if '0x' in register:
            return True
        else:
            register = register.replace("-", "", 1)
            if register.isdigit():
                return True
        return False
    pass


def parseInstruction(opcode, params):
    # Input: opcode w/ format, parameters
    # The opcode will be used to reference a format in the libs provided
    # Parameters are passed in and attempt to be written to hex.
    isValidFormat = False
    opcodeIndex = 0
    asmString = ""
    asmList = [None] * len(params)
    asmListNumList = [None] * 4

    for i in range(len(opcodeFormats)):
        if opcode == opcodeFormats[i][0]:
            # If parameters are valid, write first identifier to file and set to true
            isValidFormat = True
            opcodeIndex = i
            asmString += opcodeFormats[i][1]
            # print(asmString)
        pass
    if isValidFormat is False:
        # If parameters are not valid, print which line in the input file throws an error
        return

    # Create a bytearray, so we can write binary to the file
    for i in range(3):
        if not validateReg(params[i], i):
            # if imm and register is not valid, stop here, print error on the line
            return
        else:
            # if valid, write the value here
            binWrite = int(params[i].replace("$", "", 1))
            # print(opcodeFormats[opcodeIndex][i+2].format(binWrite))
            if binWrite < 0:
                binWrite = 65535 - abs(binWrite) + 1
                # print(hex(binWrite))
                pass
            # asmListNumList[i] = binWrite
            asmList[i] = opcodeFormats[opcodeIndex][i+2].format(binWrite)
            # asmString += opcodeFormats[opcodeIndex][opcodeData[opcodeIndex][i+1]].format(binWrite)
            # print(bin(int(opcodeFormats[opcodeIndex][i+2].format(binWrite))))
            pass
        pass

    for i in range(len(opcodeData[opcodeIndex])-1):
        asmString += asmList[opcodeData[opcodeIndex][i+1]]
        pass
    if (len(opcodeFormats[opcodeIndex]) > 5):
        asmString += '{0:05b}'.format(opcodeFormats[opcodeIndex][5]) + '{0:05b}'.format(opcodeFormats[opcodeIndex][6])
        pass
    # outputFile.write(finalWrite)
    # chop the string into 4 pieces (length of binary)
    # write to bytes with 0b in front
    # convert to int
    # write as binary to file
    # outputFile.write(bytes(int(asmList[opcodeData[opcodeIndex][i+1]], 2)))
    # 00000000 01000011 00001000 00100000
    # 00010000 01100100 11111111 11111110
    # asmListNumList[0] = int(asmString[:8], 2)
    # asmListNumList[1] = int(asmString[9:17], 2)
    # asmListNumList[2] = int(asmString[18:25], 2)
    # asmListNumList[3] = int(asmString[26:], 2)
    fix = 0
    if opcodeFormats[opcodeIndex][0] == 'beq':
        # Find out why this is happening please
        fix = 1
        pass
    asmListNumList[0] = int(asmString[:7+fix], 2)
    asmListNumList[1] = int(asmString[8:16], 2)
    asmListNumList[2] = int(asmString[17:24+fix], 2)
    asmListNumList[3] = int(asmString[25-fix:], 2)

    # print(str(bin(asmListNumList[0])) + " " + str(bin(asmListNumList[1])) + " " + str(bin(asmListNumList[2])) + " " + str(bin(asmListNumList[3])))

    # for i in range(4):
    #     print(str(bin(asmListNumList[i])) + " ")
    print(asmString)
    finalByteArr = bytearray(asmListNumList)
    conversion = bytes(finalByteArr)
    outputFile.write(conversion)



    # for i in range(4):
    #     outputFile.write(asmListNumList[i])
    # print(asmString)


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
        if params.find('0x') != -1:
            tempList = params.strip().split(', ')
            paramsArray = [tempList[0], tempList[1].partition("(")[0], tempList[1].partition("(")[2].partition(")")[0]]
            pass
        else:
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
                parseInstruction(opcodeID, paramsArray)
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
                parseInstruction(opcodeID, paramsArray)
                pass
            case 'and':
                parseInstruction(opcodeID, paramsArray)
                pass
            case 'or':
                pass
            case 'slt':
                pass
            case 'beq':
                parseInstruction(opcodeID, paramsArray)
                pass
            case 'j':
                pass
            case _:
                pass
        if mutableData.find('\n') != -1:
            # Increment to next line here
            mutableData = mutableData[mutableData.find('\n') + 1:]
        else:
            # End the loop here
            break
        pass

    pass


if __name__ == '__main__':
    main()
