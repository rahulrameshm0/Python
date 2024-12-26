''''
weight = float(input("Enter you weight in Kg: "))
height = float(input("Enter your height in meter: "))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f"Your BMI is {round(bmi)} and you are underweight")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)} and you are normal weight")
elif bmi < 30:
    print(f"Your BMi is {round(bmi)} and you are overweight")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)} and you are obese")
elif bmi < 40:
    print(f"Your BMI is {round(bmi)} and you are clinically obese")
'''
import random

'''
year = int(input("Which year you want to check: "))
if year % 4:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")

else:
    print('Not leap year')
'''

#PIZZA ORDER

''''
size = input("What size of pizza do you want (L/M/S)? ")
bill = 0
if size == 'l' or size == 'L':
    bill += 100
    print("Large pizza price is 300")
elif size == 'm' or size == 'M':
    bill += 200
    print("Medium pizza prise is 200")
elif size == 'l' or size == 'S':
    bill += 300
    print("Small pizza price is 100")

add_pepperoni = input('Do you need Pepperoni Y/N? ')
if add_pepperoni == 'y' or add_pepperoni == 'Y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50

extra_cheese = input("Do you need extra cheese Y/N? ")
if extra_cheese == 'y' or extra_cheese == 'Y':
    bill += 20
print(f'Your total price is {bill}')

'''

#LOVE CACULATER
'''
name_1 = input('What is your name? ')
name_2 = input('What is his/her name? ')
combine = name_1 + name_2
combine_str = combine.lower()

t = combine_str.count('t')
r = combine_str.count('r')
u = combine_str.count('u')
e = combine_str.count('e')
true = t + r + u + e

l = combine_str.count('l')
o = combine_str.count('o')
v = combine_str.count('v')
e = combine_str.count('e')
love = l + o + v + e

love_score = int(str(true) + str (love))

if love_score < 10 or love_score > 90:
    print(f'your love score is {love_score} you are greate match')
elif love_score < 40 or love_score > 50:
    print(f'your love score is {love_score} you are alright together')
else:
    print(f"your love score is {love_score}")
'''

'''
row_1 =['🤩','🤩','🤩']
row_2 =['🤩','🤩','🤩']
row_3 =['🤩','🤩','🤩']
matrix =[row_1,row_2,row_3]
print(f'{row_1}\n{row_2}\n{row_3}')
position = input("Enter your position where you want to hide your money: ")
row_number = int(position [0])
column_number = int(position [1])
row_selected = matrix[row_number -1]
row_selected[column_number -1] =3200
print(f'{row_1}\n{row_2}\n{row_3}')
'''

'''
height = input("Please enter your height separated by space: ")
count = 0
heights_list = height.split()
for height in heights_list:
    count += 1
print(count)

for i in range(count):
    heights_list[i] = int(heights_list[i])

total = 0
for person in heights_list:
    total += person
avg = total / count
print('avg =',round(avg))
'''

'''
number = input('Enter the list of numbers: ')
numbers_list = number.split()
count = 0

for number in numbers_list:
    count += 1
print(f'The length of the list is : {count}')

for number in range(count):
    numbers_list[number] = int(numbers_list[number])
maximum_number = numbers_list[0]

for number in numbers_list:
    if number > maximum_number:
        maximum_number = number
print(f'The maximum from the list is : {maximum_number}')
'''
'''
import random
while True:
    user = int(input("Enter a number: "))
    if user == 0:
        print("Bye")
        break

    random_number = random.randint(0,10)

    if user > 10:
        print("You can only enter a number form is one to 10")
    elif user == random_number:
        print("You Win")
    else:
        print(f"You lose, computer choice {random_number}")
        '''

'''
total = 0
number = int(input("Enter a number: "))
while number > 0:
    total = total + number
    number = int(input("Enter a number: "))
print("total is = ",total)
'''

a = [1,2,3,4,5]
print(5 in a)