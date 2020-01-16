import math

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here
def make_change(dollar_amount):
    piggy_bank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    piggy_bank["quarters"] = int(dollar_amount // .25)
    dollar_amount %= 0.25
    piggy_bank["dimes"] = int(dollar_amount // .1)
    dollar_amount %= 0.1
    piggy_bank["nickels"] = int(dollar_amount // .05)
    dollar_amount %= 0.05
    piggy_bank["pennies"] = math.ceil(dollar_amount / .01)

    return piggy_bank

'''
>>> print(piggyBank)
{ 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }
'''
print(make_change(8.69))