'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.'''

num = int(input("Give me a number: "))
if num % 4 == 0:
    print('Your number is a multiple of 4!')
elif num % 2 == 0:
    print('Your number is even!')
else:
    print('Your number is odd!')
