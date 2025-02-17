numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]
## output: 3

# numbers[-1]
## output: 2

# numbers[3]
## output: 1

# numbers[:-1]
## output: 3, 1, 4, 1, 5, 9

# numbers[3:4]
## output: 1

# 5 in numbers
## output: 4 (True)

# 7 in numbers
## output: None (False)

# "3" in numbers
## output: None (False)

# numbers + [6, 5, 3]
## output: 3, 1, 4, 1, 5, 9, 2, 6, 5, 3

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)