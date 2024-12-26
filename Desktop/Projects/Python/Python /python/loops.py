'''for i in range(0,21,2):
   print(i)'''
import random

'''
while True:
    user_input = int(input('Enter a number: '))
    if user_input < 0:
        print('You can\'t enter a negative number')
        break'''
'''
number = int(input("Enter a number to find factorial number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f'The factorial number of {number} is {factorial}')'''
import random

'''
number = 0
while True:
    if number != 7:
        number = random.randint(1,10)
        print('Generated numbers are: ', number)
    else:
        break
print('Found 7')'''

'''
amount = 1000
while amount > 0:
    number = int(input("Enter your amount to withdraw: "))
    if number <= amount and number > 0:
        amount -= number
        print(f"Withdrawal successful, your balance is {amount}")
    else:
        print("The amount you have entered is invalid, please try different amount")
print("Thank You for using our ATM")
'''
import random

'''while True:
    user_input = int(input('Guess a number: '))
    computer = random.randint(1, 10)
    if user_input > 10:
        print("Please choose the number between 1 and 10")
    elif user_input > computer:
        print(f"You Lose, Computer choose:{computer}")
    elif user_input < computer:
        print(f"You Lose, Computer choose:{computer}")
    else:
        print("You Win!!")
'''
'''
while True:
    n_exit = input("enter exit if you need exit from the loop: ")
    if n_exit == 'exit':
        print('Than you!!, operation has been completed')
        break

    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    selection = int(input("Enter your selection: "))
    if selection == 1:
        sum = num_1 + num_2
        print(f"The total after adding these two number = {sum}")
    elif selection == 2:
        sum = num_1 - num_2
        print(f"The number after subtracting = {sum}")
    elif selection == 3:
        sum = num_1 * num_2
        print(f"The number after multiplying is = {sum}")
    elif selection == 4:
        if num_2 == 0:
            print("Zero cannot be divided")
        else:
            sum = num_1 / num_2
            print(f'Total after dividing = {sum}')
    else:
        print("The number that you have entered is invalid!")
'''
'''
for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print(f"{i} X {j} = {result}\t")
    print()
    '''

'''
for i in range(1, 11):
    print(i)
'''
'''
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in number:
    total += i
print(total)
'''
'''
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(number)-1, -1, -1):
    print(number[i])
'''
'''
total = 0
for i in range(1,10):
    total += i
    print(total)
print(f"Total is {total}")
'''

'''
for i in range(2,100):
    prime = True
    for num in range(2, i):
        if i % num == 0:
            prime = False
            break
    if prime:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
'''

'''
a = input("Enter your name: ")
b = ["Rahul", "Ramesh", "Afam", "Sreejith", "Sachin", "Bincy"]
if a in b:
    print("The Name You have entered is in the list")
else:
    print("The name is not on the list")
'''
'''
list_1 = ["Binsy", "Ramesh", "Rahul", "Rohit"]
list_2 = ["Jasim", "Afam", "Tony", "Rahul", "Rohit"]
list_3 = []
for i in list_1:
    if i in list_2:
        list_3.append(i)
print(f"The name that have in both sides are : {list_3}")

'''
'''
list_1 = []
while True:
    user_input = input("Enter a number or q to quit: ")
    if user_input == "q":
        print("Program completed, Thank You!!")
        break
    user_input = int(user_input)
    if user_input not in list_1:
        list_1.append(user_input)
    else:
       print("The number you have entered is already exited please try different number")
print(f"The total is: {list_1}")

'''
'''
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

sum = num_1 + num_2

print(f"Total = {sum}")
'''
'''
celsius = float(input("Enter the celsius"))
f =(celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {f:.2f} degrees Fahrenheit")
print(f"{celsius} degrees Celsius is equal to {f:.2f} degrees Fahrenheit")
'''

'''number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))'''

'''a = 1
number = int(input("Enter a number: "))
while True:
    if a == number:
        break
    print(a)
    a += 1
'''

'''
user_input = int(input("Enter Your mark: "))
if user_input < 0:
    print("The grade should not have negative number")
elif user_input <= 25:
    print("Your Grade is D")
elif user_input <= 45:
    print("Your grade is C")
elif user_input <= 85:
    print("Your Grade is B")
elif user_input <= 100:
    print("Your grade is A")
else:
    print("The grade should not be greater than 100")
'''

'''
user_input = input("Enter a letter: ")
if user_input == "A" or user_input == "a":
    print("A is a vowel")
elif user_input == "E" or user_input == "e":
    print("E is a vowel")
elif user_input == "I" or user_input == "i":
    print("I is a vowel")
elif user_input == "O" or user_input == "o":
    print("O is a vowel")
elif user_input == "U" or user_input == "u":
    print("U is a vowel")
else:
    print("This letter is Consonant")
'''

'''
user_input = int(input("Enter a number: "))
if user_input > 0:
    for i in range(1, 11):
        print(f"The multiplication {user_input} is {i * user_input}")
'''


'''
Congratulations! You are one more step close to Python Programming World. You are now familiar with if-elif-else in Python, and for loop in Python.

While loop in Python is same as like in CPP and Java, but, here you have to use ':' to end while statement (used to end any statement). While loop is used to iterate same as for loop, except that in while loop you can customize jump of steps in coupling with variable used to loop, after every iteration, unlike in for loop (you cannot customize jump according to the variable you are using to loop through).

Let's get it more clearly through this question. Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

'''
'''
while True:
        user_input = input("Enter a number: ")
        if user_input == "q" or user_input == "Q":
                print("Program Ended")
                break

        user_input = int(user_input)
        a = 1
        while a <= user_input:
                print(a)
                a += 1
'''
'''
a = 1
while True:
    user_input = input("Enter a number: ")
    if user_input == "q":
        break
    user_input = int(user_input)
    while a <= user_input:
        print(a)
        a += 1
'''
'''
n_input = int(input("Enter a number: "))
while True:
    if n_input <= 1:
        print(n_input)
        break
    print(n_input)
    n_input -= 1
'''
#Creating a Triangle with star
'''
user_input = int(input("Enter how many row do you need: "))
for i in range(1, user_input + 1):
    for j in range(i):
        print("X", end="")
'''

'''
user_input = int(input("Enter your age: "))
if user_input < 0:
    print("You can't give a negative value for your age.")
else:
    if user_input <18:
        print("You are a minor")
    elif user_input > 18 and user_input < 65:
        print("You are an adult")
    elif user_input > 65:
        print("You are a senior")
'''
'''
for i in range(1, 10 + 1):
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")
'''
'''
a = []
for i in range(1):
    grade_1 = int(input("Enter your grade in Math: "))
    grade_2 = int(input("Enter your grade in Physics: "))
    grade_3 = int(input("Enter your grade in Chemistry: "))
    grade_4 = int(input("Enter your grade in English: "))
    grade_5 = int(input("Enter your grade in Computer: "))
    a.append(grade_1)
    a.append(grade_2)
    a.append(grade_3)
    a.append(grade_4)
    a.append(grade_5)
total = sum(a)
average = total / len(a)

if average > 60:
    print("You passed")
else:
    print("You failed")
'''
'''
user_input = int(input("Enter a number: "))
for i in range(user_input + 1):
    if i % 3 == 0:
        print(f"{i} is divisible by 3")
        continue
    if i > 62:
        break
    print(i)

'''
'''
user_input = input("Enter a letter: ")
for i in user_input:
    if i in "a, e, i, o, u" or i in "A, E, I, O, U":
        print(f"{i} is a vowel")
    else:
        print("consonant")
'''
'''
import random
while True:
    user_input = input("Heads or tails: ")
    if user_input == "q":
        print("Nice Game!, we can play afterwords")
        break
    computer_choice = random.choice(["heads", "tails"])
    if user_input == computer_choice:
        print(f"it's {user_input} You Win!")
    else:
        print(f"it's {computer_choice} You Lose!")
    '''
'''
for i in range(1,50):
    if i % 2 == 0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")
'''

'''while True:
    user_input = int(input("Enter a number: "))
    if user_input > 0:
        print("The number is Positive")
    else:
        print("The number is Negative")'''
'''
user = int(input("Enter a number: "))
for i in range(1, user + 1):
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i} is FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} is Fizz")
    elif i % 5 == 0:
        print(f"{i} is Buzz")
    else:
        print(i)
'''
'''

a = [25,35,15,48,36,48,15,58]
total = sum(a)
print(total)
'''

'''
list_1 = []
while True:
    user_input = input("Enter a string: ")
    if user_input in list_1:
        print("The string you have entered already exit, please try a different string")
    else:
        list_1.append(user_input)
'''
''''
a = []
while True:
    user_input = input("Enter a Number 'done' to end the program: ")
    if user_input == 'done':
        break
    user_input = int(user_input)
    a.append(user_input)
total = sum(a)
grand = total / len(user_input)
print(f"The average of the entered number is {grand}")
'''
'''
a = []
while True:
    number = input("Enter a number or 'done' to finish: ")
    if number == "done":
        break
    number = int(number)
    a.append(number)
print(f"The maximum number form the list is {max(a)}")
print(f"The minimum number from the list is {min(a)}")
'''
'''num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter the second number: "))
if num_1 > num_2:
    print(f"{num_1} is the largest number")
elif num_2 > num_1:
    print(f"{num_2} is the largest number")
else:
    print("Both number's are equal")
'''
'''a = []
while True:
    user_input = int(input("Enter a number: "))
    if user_input < 0:
        print("Negative number is not allowed")
        break
    a.append(user_input)
total = sum(a)
print(f"The total of positive number = {total}")
'''
'''mark = int(input("Enter your grade: "))
if mark >= 90:
    print("Your grade is A")
elif mark >= 80:
    print("Your grade is B")
elif mark >= 70:
    print("Your grade is C")
elif mark >= 60:
    print("Your mark is D")
else:
    print("You fail")

'''
'''
for i in range(1, 50 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''
'''a = 1
num_1 = int(input("Enter a number: "))
for i in range(1, num_1 + 1):
    a *= i
    print(a)
'''
import random

'''
while True:
    num_1 = int(input("Enter a number between 1 to 100: "))
    number = random.randint(1, 100)
    if num_1 == number:
        print("You win!")
        break
    if num_1 < 0 or num_1 > 100:
        print("You can only enter a number between 1 to 100")
    else:
        print(f"You lose, computer choose {number}")
'''
'''
a = 0
vowel = "a, e, i, o, u"
num = input("Enter a string: ")
for i in num:
    if i in vowel:
        a += 1
print(f"The vowels that you have entered in the string is {a}")
'''
'''
user_input = input("Enter your name: ")

if "a" in user_input:
    print(f" in {user_input} is vowel")
elif "e" in user_input:
    print(f" in {user_input} is vowel")
elif "i" in user_input:
    print(f" in {user_input} is vowel")
elif "o" in user_input:
    print(f" in {user_input} is vowel")
elif "u" in user_input:
    print(f" in {user_input} is vowel")
else:
    print(f"There is no vowels in {user_input}, so it means this is a consonant")
'''
'''
code = "mrahul@72485m"
password = input("Enter you password: ")
if password == "":
    print("Please enter your password")
elif password == code:
    print("The password you have entered is correct")
else:
    print("The password is incorrect")
'''
'''
time = int(input("Time: "))
if 0 > time < 500:
    print("Good Morning")
elif 500 >= time < 1200:
    print("Good Afternoon")
elif 1700 >= time < 2100:
    print("Good Evening")
elif 2100 >= time < 2359:
    print("Good Night!!")
else:
    print("Entered time is invalid.")
    '''
'''
number = int(input("Enter a target number: "))
total = 0
while total < number:
    n_number = float(input(f"Enter a number(current total: {number - total}, Target: {number})"))
    #a.append(n_number)
    total += n_number

if total == number:
    print(f"congratulation! The sum equals the Target of {total}")
elif total > number:
    print(f"The The sum exceeds the Target {number} the final sum is {round(total)}")
'''
original_string = input("Enter a string: ")
reversed_string = ""
for i in range(len(original_string)-1,-1,-1):
    reversed_string += original_string[i]

if reversed_string == original_string:
 print(f"{original_string} is a palindrome")
else:
 print(f"{original_string} is not a palindrome")
