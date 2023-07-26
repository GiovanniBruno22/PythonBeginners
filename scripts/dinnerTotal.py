import random

def total_bill(amount, tip_percentage):
    '''
    Calculate the total amount due for dinner, including the tip.

    Args: amount (float): The total amount for dinner before adding the tip.
        tip_percentage (float): The tip percentage to be applied.

    Returns float: The total amount due, including the tip.
    '''
    tip_payable = amount * tip_percentage/100
    sum_owed = amount + tip_payable
    return sum_owed

def random_bill_amount():
    '''
    Generate a randomized total amount for dinner. 
    returns float: A randomized dinner amount between $10 and $200
    '''
    return round(random.uniform(10, 200),2)


def main():
    '''
    This function generates a randomized dinner amount, takes user input for the tip percentage,
    calculates the total amount due, and shows the change to be given back to the user.
    '''
    print("Here is your Bill")
    dinner_bill = random_bill_amount()

    print(f"dinner amount is: {dinner_bill}" )

    user_tip = float(input("How much would you like to tip? "))
    total_due =total_bill(dinner_bill,user_tip)

    print(f"Total due (including tip): {total_due}")

    amount_payable =float(input("Enter amount you are paying with:"))

    if amount_payable >= total_due:
        change = round(amount_payable - total_due,2)
        print(f"Thank you for your payment. Your change is: {change}")
    else:
        print("The amount paid is insufficient. Please pay the full amount.")

if __name__ == "__main__":
    main()


