'''
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []

user_num = int(input('Give me your number: '))

for num in a:
    if num < user_num:
        x.append(num)

print(x)
