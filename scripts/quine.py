#Imports
import os

#Prints the contents of this file using the current working directory
def print_contents():
    print(open(f'{os.getcwd()}\\quine.py', "r").read())

#Some sample code to show that the print contents function works
def sample_code():
    print(9 + 18)
    print ("This is a string")
    return "The meaning of life", 42

#Run main() when this file is executed
if __name__ == "__main__":
    print_contents()