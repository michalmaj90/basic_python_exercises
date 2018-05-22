'''Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

name = input("What's your name?? ")
age = input("What's your age?? ")
number = input("Please give me a number: ")
year = str((100 - int(age)) + 2018)
print(int(number)*("Hello " + name + "! You'll be 100 years old in " + year + '\n'))
