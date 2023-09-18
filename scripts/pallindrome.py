def is_symmetrical(input_str):
    input_str = input_str.lower()  # Convert to lowercase for case-insensitive comparison
    length = len(input_str)
    midpoint = length // 2

    for i in range(midpoint):
        if input_str[i] != input_str[length - i - 1]:
            return False
    return True

user_input = input("Enter a string: ")
if is_symmetrical(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
