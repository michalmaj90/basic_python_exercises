# Challenge
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What's your name?? ")
age = input("What's your age?? ")
year = str((100 - int(age)) + 2018)
print("Hello " + name + "! You'll be 100 years old in " + year)
