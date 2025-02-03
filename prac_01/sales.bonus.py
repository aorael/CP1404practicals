"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MINIMUM_SALES = 0
SALES_THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALES:
    if sales >= SALES_THRESHOLD:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.1
    bonus = sales * bonus_rate
    print(bonus)
    sales = float(input("Enter sales: $"))

# CHECKING
# declare bonus rate as constant
MINIMUM_DISCOUNT = 0.1
MAXIMUM_DISCOUNT = 0.15
MINIMUM_SALES = 0
SALES_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALES:
    if sales >= SALES_THRESHOLD:
        bonus_rate = MAXIMUM_DISCOUNT
    else:
        bonus_rate = MINIMUM_DISCOUNT
    bonus = sales * bonus_rate
    print(bonus)
    sales = float(input("Enter sales: $"))