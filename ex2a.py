'''Extras:
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
num = int(input("Give me a number: "))
check = int(input("Give me a second number: "))

if check % num == 0:
    print("Your second number divides evenly into num!")
else:
    print("Your second number doesn't divide evenly into num!")
