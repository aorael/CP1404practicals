"""
a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
"""
def main_a():
    for i in range(0, 100, 10):
        print(i, end = " ")
main_a()

#CHECKING
# can
for i in range(0, 101, 10):
    print(i, end=" ")

"""
b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""

def main_b():
    numbers = []
    for i in range(1, 20+1):
        numbers.append(i)
    numbers.reverse()

    for number in numbers:
        print(number, end = " ")
main_b()

#CHECKING
# can
for i in range(20,0,-1):
    print(i, end=" ")
print()

"""
c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
"""
def main_c():
    number_of_stars = int(input("Number of stars: "))
    for star in range(number_of_stars):
        print("*", end="")
main_c()

#CHECKING
#  ???

"""
d. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line.
"""
def main_d():
    number_of_stars = 4 ### E.g., if the user entered 4
    for star in range(1, number_of_stars +1):
        print(star * "*", sep="")
main_d()

#CHECKING
# can
number_of_stars = 4
for i in range(0, number_of_stars, 1):
    print("*" * i+1)
print()