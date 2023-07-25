import random

def total_bill(amount, tip_percentage):
    tip_payable = amount * tip_percentage
    sum_owed = amount + tip_payable
    return sum_owed

def random_bill_amount():
    return round(random.uniform(10, 200),2)

print("Here is your Bill")
dinner_bill = random_bill_amount()

print(f"dinner amount is: {dinner_bill}" )

user_tip = float(input("How much would you like to tip? "))

