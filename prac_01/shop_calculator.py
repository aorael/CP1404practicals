total_price = 0
MINIMUM_ITEM_NUMBER = 0
MAXIMUM_THRESHOLD = 100
DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items < MINIMUM_ITEM_NUMBER:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price -= (total_price * DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

# CHECKING
# can, total_price > 100 use constant
total_price = 0
MINIMUM_ITEM_NUMBER = 0
MAXIMUM_THRESHOLD = 100
DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
while number_of_items < MINIMUM_ITEM_NUMBER:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > MAXIMUM_THRESHOLD:
    total_price -= (total_price * DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
