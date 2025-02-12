import random

print(random.randint(5,20))
print(random.randrange(3,10, 2))
print(random.uniform(2.5, 5.5))

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# >>> it prints a random integer ranging from 5 to 20
# >>> the smallest number is 5 and the largest is 20

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# >>> it prints a random number ranging from 3 to 10 with interval value 2
# >>> the smallest number is 3 and the largest is 9
# >>> line 2 can't produce 4 because it starts from 3 and the next value is added by 2 resulting in 5 as the next number

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# >>> it prints a random float ranging from 2.5 to 5.5
# >>> the smallest number is 2.5 and largest number is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,100))
