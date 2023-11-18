"""Password generator"""

import secrets
import string
import sys
    

def main():
    """Main generator for the program"""
    try:
        length: int = int(input("Enter the length of the password: ")) # Taking user input about the length of password
    except ValueError:
        print("Not a valid number.")
        sys.exit()

    alphabet: string = string.ascii_letters + string.digits + string.punctuation # character to be used in password

    password: str = "".join(secrets.choice(alphabet) for i in range(length)) # generating the password

    print("Password is: " + password)

if __name__ == "__main__":
    main()
