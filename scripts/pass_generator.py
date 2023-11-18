"""Password generator"""

import random
import string


def generate_password(length: int = 8) -> str:
    """Generates a random password of a specified length.
    Returns a password as a string."""
    
    if length < 4:
        raise ValueError("Password length must be at least 4 to ensure all categories.")
    
    uppercase_letters: str = string.ascii_uppercase
    lowercase_letters: str = string.ascii_lowercase
    digits: str = string.digits
    punctuation: str = string.punctuation

    # Make sure each category is represented in the password
    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(punctuation)
        + ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - 4))
    )

    # Shuffle the password to randomize the order of the first four characters
    password_list: list[str] = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == '__main__':
    try:
       password_length: int = int(input("Enter the length of the password greater than 3: "))
       password: str = generate_password(password_length)
       print("Generated Password:\n", password)
    except ValueError:
        print("Invalid input. Please enter an integer greater than 4 for the password length.")
