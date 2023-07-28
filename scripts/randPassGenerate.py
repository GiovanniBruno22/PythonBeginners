import secrets
import string
    

def main():

    passCodeLength = int(input("Enter the length of the password: "))   # Taking user input about the length of password

    alphabet = string.ascii_letters + string.digits + string.punctuation    # Defining alphanumeric and special characters to be used in password

    password = ''.join(secrets.choice(alphabet) for i in range(passCodeLength))     # Creating the password

    print("Password is: " + password)

if __name__ == "__main__":
    main()
