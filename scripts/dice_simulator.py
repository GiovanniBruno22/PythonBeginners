"""
Dice Roller

Roll an amount of dice with an amount of sides chosen by the user.
"""

import random

def main():
    """The main function of the program.
    Ask the user how many dice, an roll that many dice."""
    print('How many dice would you like to roll?')

    try:
        amount_of_dice = int(input('> ')) # try to convert the answer to an int
    except ValueError:
        print('Not a valid number.') # if it doesn't work, return 'y'
        return 'y' # returning this causes the prgram to run again

    print('How many sides should the dice have?')

    try:
        amount_of_sides = int(input('> ')) # same as above, pretty much
    except ValueError:
        print('Not a valid number.')
        return 'y'

    total = 0

    for i in range(amount_of_dice):
        # add a random number between 1 and the number of sides to the total
        total += random.randint(1, amount_of_sides)

    print('Total:', total)

    again = ''
    while again not in ['y', 'n']:
        print('Would you like to go again? (Y/N)')
        again = input('> ').lower()

    return again

while True:
    if main() == 'n': # if the user does not want to play again,
        break # stop and exit

print('Thanks for playing!')