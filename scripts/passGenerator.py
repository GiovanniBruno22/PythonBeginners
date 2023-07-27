import random
import string

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


password_length = int(input("Enter the length of the password greater than 3: "))
if password_length < 4:
    raise ValueError("Password length must be at least 4.")
passwordd = generate_password(password_length)
print("Generated Password:", passwordd)
