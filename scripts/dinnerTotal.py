import random

def total_bill(amount, tip_percentage):
    tip_payable = amount * tip_percentage/100
    sum_owed = amount + tip_payable
    return sum_owed

def random_bill_amount():
    return round(random.uniform(10, 200),2)

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




