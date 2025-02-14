"""
Question 1
Write code that asks the user for their name, then opens a file
called name.txt and writes that name to it. Use open and close for
this question.
"""
def main1():
    name = input("Enter a name: ")
    out_file = open("name.txt", "w")
    print(name, file=out_file)
    out_file.close()
main1()

"""
Question 2
In the same file, but as if it were a separate program, write code that opens "name.txt" 
and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.
"""
def main2():
    in_file = open("name.txt", "r")
    print(f"Hi {in_file.readline().strip()}!")
    in_file.close()
main2()

"""
Question 3
Create a text file called numbers.txt and save it in your prac directory. 
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens numbers.txt, reads only the first two numbers, 
adds them together then prints the result, which should be... 59. 
Use with instead of open and close for this question.
"""
def main3():
    with open("numbers.txt", "r") as in_file:
        list = in_file.readlines()
        number = 0

        for i in range(2):
            number_in_file = int(list[i].strip())
            number += number_in_file
        print(number)
main3()

"""
Question 4
Now write a fourth block of code that prints the total for all lines in numbers.txt. 
This should work for a file with any number of numbers. 
Use with instead of open and close for this question.
"""
def main4():
    with open("numbers.txt", "r") as in_file:
        total = 0
        for line in in_file:
            number = int(line.strip())
            total += number
        print(total)
main4()
