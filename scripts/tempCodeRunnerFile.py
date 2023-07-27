import random
import string


# Generates a random password of a specified length.
# (int)length, which indicates the desired length of the password.
# returns a password as a string.
def generate_password(length):
    
    if length < 4:
        raise ValueError("Password length must be at least 4 to ensure all categories.")
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    # Make sure each category is represented in the password
    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(punctuation)
        + ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - 4))
    )

    # Shuffle the password to randomize the order of the first four characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == '__main__':
    try:
       password_length = int(input("Enter the length of the password greater than 3: "))
       passwordd = generate_password(password_length)
       print("Generated Password:", passwordd)
    except ValueError as e:
        print("Error: ", e)