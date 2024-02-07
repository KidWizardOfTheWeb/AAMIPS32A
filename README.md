# AAMIPS32A

## **A**nother **A**mateur **MIPS32** **A**ssembler
This is an implementation of a simple MIPS32 assembler intended to be modular enough to add commands. 

Using dictionaries, the program reads in an entire file and proceeds to parse it based on definitions from the libraries included. 
The program converts from MIPS32 to hex and then to binary. It cannot convert vice versa.

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
