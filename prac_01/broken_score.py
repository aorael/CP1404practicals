"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

#CHECKING
# can
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
message = ""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= EXCELLENT_THRESHOLD:
        print("Excellent")
    elif score >= PASS_THRESHOLD:
        print("Passable")
    else:
        print("Bad")