# AAMIPS32A

## **A**nother **A**mateur **MIPS32** **A**ssembler
This is an implementation of a simple MIPS32 assembler intended to be modular enough to add commands. 

Using an array of tuples, the program reads in an entire file and proceeds to parse it based on definitions from the opcodes included. 
The program converts from MIPS32 to binary. It cannot convert vice versa.

# Running the program
To run, invoke the `ASMain.py` file with two command line arguments.
The two command line arguments:
> Input file name (including extension). Usually ends in `.s`
> 
> Output file name (including extension). Ends in `.dat`

Example command (using provided test file):
```commandline
py ASMain.py abc.s output.dat
```

# Documentation for reference
## Instructions:
```commandline
load word (lw): 
    example: lw $rt, imm($rs)
    parsing:
        lw passed as string
        $rt checks for $ sign, then checks which register is being used for return val
        , sign is checked, then immediate value is read
        $rs is checked inside of parenthesis, checks register that is being used
```
```commandline
store word (sw):
    example: sw $rt, imm($rs)
        parsing:
            sw passed as string
            $rt checks for $ sign, then checks which register is being used for return val
            , sign is checked, then immediate value is read
            $rs is checked inside of parenthesis, checks register that is being used
```
```commandline
add:
    example: add $rd, $rs, $rt
        parsing:
            $rd checks register for return val
            $rs checks reg param 1 being added
            $rt checks reg param 2 being added
```
```commandline
sub:
    example: sub $rd, $rs, $rt
        parsing:
            $rd checks register for return val
            $rs checks reg param 1 being subtracted
            $rt checks reg param 2 being subtracted

```
```commandline
and:
    example: $rd, $rs, $rt
        parsing:
            $rd checks register for return val
            $rs checks reg param 1 for comparison
            $rt checks reg param 2 for comparison
```
```commandline
or:
    example: $rd, $rs, $rt
        parsing:
            $rd checks register for return val
            $rs checks reg param 1 for comparison
            $rt checks reg param 2 for comparison
```
```commandline
slt:
    example: $rd, $rs, $rt
        parsing:
            $rd checks register for return val
            $rs checks reg param 1 for comparison
            $rt checks reg param 2 for comparison
```
```commandline
branch if equal (beq)
    example: $rs, $rt, imm
        parsing:
        $rs checks reg param 1 for comparison
        $rt checks reg param 2 for comparison
        imm branches to this value if equal
```
```commandline
jump (j)
    example: address
    parsing:
        address is the value to jump to
```
