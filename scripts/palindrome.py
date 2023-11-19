"""Palindrome
Tell the user if the string that they enter is a palindrome.
"""

def is_palindrome(input_str: str = "kayak") -> bool:
    """Check if a string is a palindrome"""
    input_str = input_str.lower()  # Convert to lowercase for case-insensitive comparison
    return list(input_str) == list(reversed(input_str))

def main() -> None:
    """Main program function"""
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
    
    again = input("Would you like to go again? (y/n): ").lower()
    if again.startswith("y"):
        main()
    else:
        print("Thanks for playing!")
        return

if __name__ == '__main__':
    main()
