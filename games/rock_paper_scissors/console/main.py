"""A rock paper scissors game in Python using the 
command line
"""

import random


def rock_paper_scissors():
    r = "rock"
    p = "paper"
    s = "scissor"
    all_choices = (r, p, s)

    user = input(f"Enter a choice ({r}, {p}, {s}): ")

    if user not in all_choices:
        print(f"Invalid choice....!!!")
        return

    computer = random.choice(all_choices)

    print(f"User chose {user}, and the computer chose {computer}")

    if user == computer:
        print(f"It's tie...")
    elif ((user == r and computer == s) or (user == p and computer == r)  or (user == s and computer == p)):
        print(f"You won!")
    else:
        print(f"You lost!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again.startswith("y"):
        rock_paper_scissors()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    rock_paper_scissors()