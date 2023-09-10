def base_converter(num, base):
    if base == "bin".lower():
        return bin(num)[2:]
    elif base == "hex".lower():
        return hex(num)[2:]
    elif base == "oct".lower():
        return oct(num)[2:]
    else:
        return "uncorrect base"
    
if __name__ == "__main__":
    num = int(input("Enter a number that you want to convert: "))
    base = input("Enter base to that you want to convert: ")
    try:
        print(f"Your result is {base_converter(num, base)}")
    except ValueError:
        print("Value cannot be converted to that base!")