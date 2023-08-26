# Basic calculator functions that take two numbers
def add(a,b): 
    return a + b

def subtract(a,b): 
    return a - b

def multiply(a,b): 
    return a * b

def divide(a,b): 
    return a / b


# Defining variables from user input
# Note: input() returns a string, so we need to convert to int for numbers
a = int(input('What is your first number? '))
b = int(input('What is your second number? '))
c = input('What operation would you like to perform (add, subtract, multiply or divide)? ')

# Calling the appropriate function based on user input
# Returning the result as an f-string
if c == 'add':
    print(f'result: {add(a,b)}')
elif c == 'subtract':
    print(f'result: {subtract(a,b)}')
elif c == 'multiply':
    print(f'result: {multiply(a,b)}')
elif c == 'divide':
    print(f'result: {divide(a,b)}')
