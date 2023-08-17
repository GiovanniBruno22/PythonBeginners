def fizzbuzz():
    number = int(input("Choose a number: "))
    for i in range(number):
        print(i)
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

if __name__ == "__main__":
    fizzbuzz()