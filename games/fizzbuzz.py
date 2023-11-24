def fizzbuzz() -> None:
    number = input("Choose a number: ")
    
    if not number.isdecimal(): # if the entered number isn't valid
        print("That is not a valid number, please try again.")
        return
    
    number = int(number)

    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz()