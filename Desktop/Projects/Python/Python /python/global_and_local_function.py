# user_input = int(input("Enter a number: "))
# a = 2
# if user_input < a:
#     print(f"{user_input} is not a prime number")
# else:
#     while a * a <= user_input:
#         if user_input % a == 0:
#             print(f"{user_input} is not a prime number")
#             break
#         a += 1
#     else:
#         print(f"{user_input} is a prime number")
#

# user_input = int(input("Enter a number: "))
# a = 1
# for i in range(1, user_input + 1):
#     a *= i
# print(f"The factorial of {user_input} is {a}")

# list_1 = []
# while True:
#     user_input = input("Enter a number: ")
#     if user_input == "q":
#         print("Program exit! Thank You.")
#         break
#     else:
#         user_input = int(user_input)
#         list_1.append(user_input)
# total = sum(list_1)
# print(f"Your total is total is {total}")

# user_input = input("Enter a number: ")
# reversed_input = ""
# for i in range(len(user_input)-1, -1, -1):
#     reversed_input += user_input[i]
# if user_input == reversed_input:
#     print(f"{user_input} is a palindrome")
# else:
#     print(f"{user_input} is not a palindrome")

# list1 = []
# user_input = int(input("Enter  a number to find the factor: "))
# for i in range(1, user_input):
#     if user_input % i == 0:
#         list1.append(i)
# print(f"The factors of {user_input} are {list1}")

# user_input = int(input("Enter a number: "))
# for i in range(1,user_input + 1):
#     print(f"{user_input} * {i} = {user_input * i}")

# list1 = []
# while True:
#     user_input = input("Enter a number to find the largest number: ")
#     if user_input == "q":
#         break
#     else:
#         user_input = int(user_input)
#         list1.append(user_input)
#
# print(f"The largest number is {max(list1)}")

# list1 = []
# while True:
#     user_input = input("Enter a number: ")
#     if user_input == "q":
#         break
#     else:
#         user_input = int(user_input)
#     if user_input % 2 == 0:
#         list1.append(user_input)
# print(f"The even numbers are: {list1}")

# a = 1
# user_input = int(input("Enter a number: "))
# for i in range(1, user_input + 1):
#        a *= i
# print(f"The factorial of {user_input} is {a}")


# a = 0
# vowels = "aeiou"
# user_input = input("Enter a string: ")
# for i in vowels:
#     if i in user_input:
#         a += 1
# print(f"{user_input} has {a} vowel")

# LEAP YEAR

# user_input = int(input("Enter a year weather it leap year or not: "))
# if user_input % 400 == 0:
#     print(f"{user_input} is a leap year")
# elif user_input % 100 == 0:
#     print(f"{user_input} is not a leap year")
# elif user_input % 4 == 0:
#     print(f"{user_input} is a leap year")
# else:
#     print(f"{user_input} is not a leap year")

# a = {
#     "Name": "Rahul",
#     "Age": 25,
#     "Id": 251565,
#     "Mark": 95,
#     "Contact": {"Home": 9544984479, "Work": 9995999459}
# }

# user_input = int(input("Enter a number: "))
# is_prime = True
# for i in range(2, user_input):
#     if user_input % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{user_input} is a prime number")
# else:
#     print(f"{user_input} is not a prime number")


# user_input = int(input("Enter a number: "))
# a = 2
# is_prime = True
# while a < user_input:
#     if user_input % a == 0:
#         is_prime = False
#         break
#     a += 1
# if is_prime:
#     print(f"{user_input} is a prime number")
# else:
#     print(f"{user_input} is not a prime number")

# user_input = int(input("Enter a number: "))
# a = 1
# for i in range(1, user_input + 1):
#     a *= i
# print(f"The factorial of {user_input} is {a}")

# user_input = input("Enter a string: ")
# reversed_string = ""
# for i in range(len(user_input)-1, -1, -1):
#     reversed_string += user_input[i]
# if user_input == reversed_string:
#     print(f"{user_input} is a palindrome")
# else:
#     print(f"{user_input} is not a palindrome")

# def add(num1,num2):
#     return num1 + num2
# print(add(2,15)

# def even_number():
#     num_1 = int(input("Enter the 1st number: "))
#     num_2 = int(input("Enter the 2nd number: "))
#     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
#     user_input = int(input("Enter your choice: "))
#     if user_input == 1:
#         total = num_1 + num_2
#         return f"{num_1} + {num_2} = {total}"
#     elif user_input == 2:
#         total = num_1 - num_2
#         return f"{num_1} - {num_2} = {total}"
#     elif user_input == 3:
#         total = num_1 * num_2
#         return f"{num_1} * {num_2} = {total}"
#     elif user_input == 4:
#         if num_2 == 0:
#             print("Error occurred!! you cannot divide by zero")
#     else:
#         total = num_1 / num_2
#         return f"{num_1} / {num_2} = {total}"
# print(even_number())

# def maximum_number(num1, num2):
#     if num1 == num2:
#        return "The number is equal"
#     elif num1 > num2:
#         return f"{num1} is the largest number"
#     else:
#         return f"{num2} is the largest number"
# print(maximum_number(245,55))

# def prime_check():
#     user_input = int(input("Enter a number: "))
#     if user_input < 2:
#         return f"{user_input} is not prime"
#     is_prime = True
#     for i in range(2, user_input):
#         if user_input % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         return f"{user_input} is a prime number"
#     else:
#         return f"{user_input} is not prime number"
# print(prime_check())


# def maximum(num1, num2, num3):
#     if num3 > num2 and num3 > num1:
#         return f"{num3} is the largest number"
#     elif num1 > num2 and num1 > num3:
#         return f"{num1} is the largest number"
#     elif num1 == num2 and num1 == num3:
#         return f"The numbers are equal"
#     else:
#         return f"{num2} is the largest number"
# print(maximum(955,955,955))

# user_input_1 = int(input("Enter 1st number: "))
# user_input_2 = int(input("Enter 2nd number: "))

# def multiply_and_add():
#     product = user_input_1 * user_input_2
#     if product <= 1000:
#         return product
#     else:
#         return user_input_1 + user_input_2
# print(multiply_and_add())

# user_input = int(input("Enter a number: "))
# total = 0
# previous_number = 0
# for i in range(0, user_input + 1):
#     total += i
#     print(f"Current number {i} previous number {previous_number} The sum is {total}")
#     previous_number = i

'''
Write a Python code to accept a string from the user and display characters present at an even index number.
For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
'''

# user_input = input("Enter a string: ")
# for i in range(0, len(user_input), 2):
#     print(f"The original string is {user_input}")
#     print(user_input[i])

# def first_last_same(numberList):
#     print(f"Given_list: {numberList}")
#     first_num = numberList[0]
#     last_num = numberList[-1]
#     if first_num == last_num:
#         return True
#     else:
#         return False
# number_list_1 = [10,20,30,40,10]
# print(f"The result is {first_last_same(number_list_1)}")
#
# number_list_2 = [10,20,40,45,35]
# print(f"The result is {first_last_same(number_list_2)}")


# def divisible_check():
#     number_y = [5, 12, 15, 25, 35, 47, 56]
#     print(f"Given list is {number_y}")
#     print("Divisible by 5")
#     for num in number_y:
#         if num % 5 == 0:
#             print(num)
# print(divisible_check())


# str_x = "Emma is a good developer. Emma is a good writer"
# count = str_x.count("Emma")
# print(count)

# for i in range(1, 5 + 1):
#     for j in range(i):
#         print(i, end="")
#     print()

# def palindrome():
#     user_input = input("Enter a string: ")
#     reversed_string = ""
#
#     for i in range(len(user_input)-1, -1, -1):
#         reversed_string += user_input[i]
#     if reversed_string == user_input:
#         return "YES, The given name is a palindrome"
#     else:
#         return "NO, The given name is not a palindrome"
# print(palindrome())


# for multiplication in range(1, 11):
#     for j in range(1, 11):
#         print(f"{multiplication} * {j} = {multiplication * j}")
#     print("\t")

# num1 = int(input("Enter a number: "))
# for i in range(1, num1, -1):
#     print(i)

# contact = {"Rahul": 9496320858,
#            "Rohit": 9037579459,
#            "Ramesh":9995999459
#            }
#
# def add_contact(name, number):
#

# Initialize the contacts dictionary
# contacts = {
#     "John": "555-1234",
#     "Mary": "555-5678",
#     "Bob": "555-4321"
# }

# def add_contact(name,number):
#     contacts[name] = number
#     print(f"added {name} with the number {number}")
# def display_contact():
#     print("Contact List:")
#     for name, number in contacts.items():
#         print(f"{name}: {number}")
# print("Initialize contact")
# display_contact()
#
# add_contact("martin",987545252)
# add_contact("John",65698522)
#
# print("\nContact after adding")
# display_contact()
# display_contact()


# balance = 2595.60
#
# while True:
#     try:
#         deposit = float(input("Deposit: "))
#         break
#     except:
#         print("Must be a valid quantity")
# balance += deposit
# print(f"Balance: {balance}")

# amount = 1500
# print(f"Amount: {amount}")
# while True:
#     try:
#         num = int(input("Withdraw: "))
#         break
#     except:
#         print("Please enter a valid number")
# amount -= num
#
# print(f"Balance: {amount}")

# while True:
#     try:
#         user_input = int(input(f"Enter you age: "))
#         break
#     except:
#         print("value is invalid")
# print("The age is", user_input)

# product = 555
# while True:
#     try:
#         user_input = int(input("Enter the price of the product: "))
#         if user_input == product:
#             print("Thank You")
#             break
#         print("The amount is invalid")
#
#     except ValueError:
#         print("Please enter a valid number")


#
# while True:
#     try:
#         user_input = int(input("Enter the number of item: "))
#         if user_input < 0:
#             print("You can't enter a number that is negative")
#         else:
#             print(f"The number of item is {user_input}")
#             break
#     except ValueError:
#         print("Please enter a valid number")
#
# while True:
#     user_input_1 = input("Enter a number: ")
#     try:
#         user_input_2 = float(user_input_1)
#         if '.' in user_input_1:
#             print("The number is invalid, please try a different number")
#         else:
#             user_input_1 = int(user_input_2)
#             print(f"The number is {user_input_1}")
#             break
#     except ValueError:
#         print("The value is invalid")


# def greet(name,department):
#     print("Hello",name)
#     print(f"Are you in the {department} department?")
# greet("Rahul","CS")
# greet("Jenny","CS")

# def add_numbers(num1,num2):
#     return num1 + num2
# print(add_numbers(5,15))

# def calculate_area(length,width):
#     return length * width
# print(calculate_area(10,15))


# def calculate_discount(num1, num2 = 10):
#  return num1 * (1 - num2 / 100)
# print(calculate_discount(100,20))

# def describe_pet(dog,name):
#     return f"I have a {dog} named {name}"
# print(describe_pet(dog = "dog", name = "Enzo"))
# input("Enter a string")
# def list_squares(numbers):
#     return [n ** 2 for n in numbers]
# print(list_squares([1,2,3,4])

# def add(num1,num2):
#     total = num1 + num2
#     return total
# result = add(25,38)
# print(result)

# message = "How you doing?"
# def greet():
#     global message
#     message = "How are you"
#     print("Message inside the function,", message)
# greet()
# print("Message outside the function,",message)




# def sum_of_evens():
#     list1 = []
#     while True:
#         user_input = input("Enter a number (or 'q' to quit): ")
#         if user_input == "q":
#             break
#         try:
#             user_input = int(user_input)
#             list1.append(user_input)
#         except ValueError:
#             print("Please enter a valid number.")
#
#     even_sum = 0
#     for num in list1:
#         if num % 2 == 0:
#             even_sum += num
#     print(f"The list of number are {list1}")
#     return f"The sum of even numbers is: {even_sum}"
#
# print(sum_of_evens())

# def count_pos_beg():
#     list1 = []
#     while True:
#         user_input = input("Enter a number or 'q' to quit: ")
#         if user_input == "q":
#             print("Program Exit")
#             break
#         try:
#             user_input = int(user_input)
#             list1.append(user_input)
#         except:
#             print("Enter a valid number")
#         positive_count = 0
#         negative_count = 0
#         for num in list1:
#             if num > 0:
#               positive_count += 1
#             elif num < 0:
#                 negative_count += 1
#     return f"The list of numbers are: {list1} the count of positive numbers are: {positive_count}, negative count: {negative_count}"
# print(count_pos_beg())
#


# dict_1 = {}
# def menu():
#     print("Menu:\n1.Add Student\n2.Get Student\n3.Exit")
#     user_input = input("Enter your choice: ")
#     return user_input
#
# def main_def():
#     while True:
#
#         user_input = menu()
#         if user_input == '3':
#             print("Program Exist")
#             break
#         if not user_input.isdigit():
#             print("The value you have entered is invalid")
#             continue
#         user_input = int(user_input)
#         user_input = user_input + 1
#         print("Hello")
#         if user_input == 1:
#             user_input_2 = input("Enter Student Name: ")
#             user_input_3 = int(input("Enter Student Grade: "))
#             dict_1[user_input_2] = user_input_3
#
#         elif user_input > 3:
#             print("You can only choose the option from 1 to 3")
#         elif user_input == 2:
#             user_input_2 = input("Enter Student Name: ")
#             student = student_grade(user_input_2)
#             print(student)
# def student_grade(name):
#     return f"{name} grade is {dict_1.get(name)}"
# print(main_def())



# def palindrome_check():
#     reversed_string = ""
#     user_input = input("Enter a string: ")
#     for i in range(len(user_input)-1, -1, -1):
#         reversed_string += user_input[i]
#     if user_input == reversed_string:
#         return True
#     else:
#         return False
# print(palindrome_check())

# l1 = [1,2,3,4,5,6,7,8,9,10]
# #l2 = [1,2,3,4,5,6,7,8,9]
# l2 = l1
# if l1 == l2:
#     print(True)
# else:
#     print(False)

# def prime_check():
#     user_input = int(input("Enter a number: "))
#     is_prime = True
#     for prime in range(2, user_input):
#         if user_input % prime == 0:
#             is_prime = False
#             break
#     if is_prime:
#         return f"{user_input} is a prime number"
#     else:
#         return f"{user_input} is not a prime number"
# print(prime_check())

# def factorial_check():
#     factorial = 1
#     user_input = input("Enter a number: ")
#     if not user_input.isdigit():
#         print("The value is invalid")
#     else:
#         user_input = int(user_input)
#         for i in range(1,user_input + 1):
#             factorial *= i
#         return f"The factorial of {user_input} is {factorial}"
# print(factorial_check())

# dict_1 ={}
# while True:
#     user_1 = input("Enter a key (or 'q' to quit): ")
#     if user_1 == 'q':
#         print(f"Existing and printing the final dictionary")
#         print(f"The final dictionary is {dict_1}")
#         break
#
#     user_2 = input("Enter a value for the key: ")
#     dict_1[user_1] = user_2

# user_input = int(input("Enter a number: "))
#
# if user_input % 2 == 0:
#     print("Not wierd")
# else:
#     print("Weird")

# def create_dictionary():
#     data = {"Name": "Rahul",
#             "Age": 25,
#             "Subject": {
#                 "Math": 55,
#                 "Physics": 66,
#                 "Chemistry": 75
#             }
#             }
#     subject = 'Chemistry'
#     marks = data['Subject'][subject]
#     return f"{data['Name']}'s marks in {subject}: {marks}"
# print(create_dictionary())

# def bank_account_management():
#     bank_account = {}
#     while True:
#         print("Menu:\n1.Create New Account\n2.View Account Balance\n3.Deposit Money\n4.Withdraw Money\n5.Exist")
#         user_input = input("Enter your choice: ")
#         if not user_input.isdigit():
#             print("The value you have entered is invalid.")
#             continue
#         user_input = int(user_input)
#         if user_input == 1:
#             user_input_2 = input("Enter Account Name: ")
#             user_input_3 = int(input("Enter Initial Balance: "))
#             bank_account[user_input_2] = user_input_3
#         elif user_input == 2:
#             user_input_2 = input("Enter Account Name: ")
#             print(f"Balance of {user_input_2}: {bank_account[user_input_2]}")
#         elif user_input == 3:
#             user_input_2 = input("Enter Account Name: ")
#             if user_input_2 in bank_account:
#                 user_input_4 = int(input("Enter Deposit Amount: "))
#                 bank_account[user_input_2] += user_input_4
#                 print(f"Deposit successful. Your balance is: {bank_account[user_input_2]}")
#             else:
#                 print("Account not found")
#         elif user_input > 5:
#             print("You can only enter the choice b/w 1 to 5")
#         elif user_input == 4:
#             user_input_2 = (input("Enter your name: "))
#             if user_input_2 in bank_account:
#                 user_input_5 = int(input("Enter how much you need to withdraw: "))
#                 if bank_account[user_input_2] >= user_input_5:
#                     bank_account[user_input_2] -= user_input_5
#                     print(f"Withdrawal Successful! Your balance is: {bank_account[user_input_2]}")
#                 else:
#                     print("You Account Balance is insufficient")
#             else:
#                 print("Account not found")
#
#         elif user_input == 5:
#             return "Exist from the bank account"
#
# print(bank_account_management())

# import random
# print("Welcome to the number guessing game!")
# print("I am thinking of a number between 1 to 100")
# while True:
#     computer_choice = random.randint(1, 100)
#     try:
#         user_input = int(input("guess a number: "))
#     except ValueError:
#         print("The value you have entered is invalid")
#         continue
#
#     if user_input > computer_choice:
#         print("Your guess is too high, Try again!!")
#     elif user_input < computer_choice:
#         print("Your guess is too low, Try again!!")
#     elif user_input == computer_choice:
#         print("your guess is correct! congratulation, you have guessed the number")
#         user_input_2 = input("Would you like to play again (yes/no): ")
#         if user_input_2 == 'yes':
#             continue
#         elif user_input_2 == 'no':
#             print("Thanks for playing! good bye!")
#             break



# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# # Example usage
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))

# dict1 = {}
#
# try:
#     user_input_1 = input("Enter a key value pair: ")
#     key1, value1 = user_input_1.split(":")
#     dict1[key1.strip()] = value1.strip()
#
#     user_input_2 = input("Enter a key value pair: ")
#     key2, value2 = user_input_2.split(":")
#     dict1[key2.strip()] = value2.strip()
#
#     user_input_3 = input("Enter a key value pair: ")
#     key3, value3 = user_input_3.split(":")
#     dict1[key3.strip()] = value3.strip()
# except ValueError:
#     print("You should add the key & value")
#
# while True:
#     user_input_4 = input("Chose an operation (Add/update/remove/view/exist): ")
#     if user_input_4 == "add":
#         try:
#             user_input_5 = input("Enter a key-value pair to add: ")
#             key4, value4 = user_input_5.split(":")
#             dict1[key4.strip()] = value4.strip()
#         except ValueError:
#             print("You should enter the key & value")
#     elif user_input_4 == "view":
#         print(f"Current Dictionary: {dict1}")
#     elif user_input_4 == "update":
#         user_input_6 = input("Enter the key you want to update: ")
#         user_input_7 = input("Enter the new value: ")
#         if user_input_6 in dict1:
#             dict1[user_input_6] = user_input_7
#         else:
#             print(f"{user_input_7} is not found")
#     elif user_input_4 == "remove":
#         user_input_8 = input("Enter the key you need to remove: ")
#         if user_input_8 in dict1:
#             dict1.pop(user_input_8)
#         else:
#             print(f"{user_input_8} is not found in the dictionary")
#
#     elif user_input_4 == "exit":
#         print("Program Exit, Thank You!!")
#         break
#     else:
#         print("Please enter the value that has given in the option")

# user_input = 10
# user_input_2 = 30
# for i in range(user_input, user_input_2 + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         if i > 1:
#             print(i)


#
# print("Welcome to simple banking system")
# print("1.Check balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")
# a = 1500
# while True:
#     try:
#         user_input = int(input("Choose an option: "))
#         if user_input == 1:
#             print(f"your current balance is {a}")
#         elif user_input == 2:
#             user_input_2 = int(input("Enter amount to deposit: "))
#             a += user_input_2
#         elif user_input == 3:
#             user_input_3 = int(input("Enter amount to withdraw: "))
#             if user_input_3 > a:
#                 print("Insufficient Balance")
#             else:
#                 a -= user_input_3
#                 print(f"{user_input_3} Rs has been withdrawn from your bank account your balance is {a}")
#         elif user_input == 4:
#             print("Exiting...Thank you for banking with us")
#             break
#         elif user_input > 4:
#             print("You can only enter the option between 1 to 4")
#     except ValueError:
#         print("The value you have entered is invalid")

# cart = {}
# print("\t")
# print("Welcome to the shipping cart system")
# print("\t")
# print("1.Add Item to Cart\n2.View cart\n3.Remove Item From cart\n4.Clear cart\n5.Exit")
# while True:
#     print("\t")
#     try:
#         user_input = float(input("Choose an option: "))
#         if user_input == 1:
#             user_input_2 = input("Enter item name: ")
#             user_input_3 = float(input("Enter item Price: "))
#             cart[user_input_2] = user_input_3
#             print("Item added to cart!")
#         elif user_input == 2:
#             print("-----Shopping Cart----")
#             for key, value in cart.items():
#                 print(f"Item: {key}, Price: {value} Rs")
#             print(f"Total: {sum(cart.values())}")
#
#         elif user_input == 3:
#             user_input_4 = input("Enter the name of the item to remove from the cart: ")
#             if user_input_4 in cart:
#                 cart.pop(user_input_4)
#                 print("Item removed from the cart")
#             else:
#                 print(f"There is no {user_input_4} found in this cart")
#
#         elif user_input == 4:
#             cart.clear()
#             print("Cart Cleared")
#         elif user_input == 5:
#             print("Exiting... Thank you for shopping with us!")
#             break
#         if user_input > 5 or user_input < 0:
#             print('You can only enter the option between 1 to 5.')
#     except ValueError:
#         print("The value you have entered is invalid")

# print("Welcome to the library management system")
# print("1.View all available books\n2.Borrow a book\n3.Return a book\n4.Add new books to the library\n5.Exit")
# library = {}
# while True:
#     try:
#         user_input = int(input("Choose an option: "))
#         if user_input == 1:
#            for value in library.keys():
#                print("*", value)
#         elif user_input == 2:
#             user_input_2 = input("Please enter the name of the book that you want borrow: ")
#             if user_input_2 in library.keys():
#                 library.pop(user_input_2)
#                 print(f"You have borrowed {user_input_2}. Enjoy reading!")
#             else:
#                 print(f"{user_input_2} is not found in the Library")
#         elif user_input == 3:
#             user_input_3 = input("Please enter the name of the book that you need to return: ")
#             library[user_input_3] = user_input_3
#             print(f"Thank you for returning {user_input_3}")
#         elif user_input == 4:
#             user_input_4 = input("Please enter the name of the book you need to add: ")
#             library[user_input_4] = user_input_4
#             print(f"{user_input_4} has been added to the library!")
#
#         elif user_input == 5:
#             print("Exiting the system. Thank you for using the Library Management System!")
#             break
#         if user_input < 0 or user_input > 5:
#             print("Please enter the options that given in the system")
#     except ValueError:
#         print("Please enter valid option")

# store = []
#
# print("Welcome to the Grocery List Manager")
# print("\t")
# print("1.Add item to list\n2.View Grocery List\n3.Remove item from list\n4.Clear grocery List\n5.Exit")
#
# while True:
#     try:
#         user_input = int(input("Enter an option: "))
#         if user_input == 1:
#             user_input_2 = input("Enter the item to add: ")
#             store.append(user_input_2)
#             print(f"{user_input_2} has beem added to the list")
#         elif user_input == 2:
#             if store:
#                 for list1 in store:
#                     print(f"* {list1}")
#             else:
#                 print("The grocery list is empty")
#         elif user_input == 3:
#             user_input_3 = input("Enter the name of the item that you need to remove for the list: ")
#             if user_input_3 in store:
#                 store.remove(user_input_3)
#                 print(f"{user_input_3} has been removed from the list")
#             else:
#                 print(f"{user_input_3} is not found in the list")
#         elif user_input == 4:
#             if store:
#                 store.clear()
#                 print("The list has been cleared!")
#             else:
#                 print("There is no items to be cleared in the list")
#         elif user_input == 5:
#             print("Exiting! Thank You for using Grocery List Manager")
#             break
#         else:
#             print("You can only enter the number between 1 to 5")
#
#     except ValueError:
#         print("The value you have entered is invalid")

import random
#
# print("Welcome to the quiz!")
# score = 0
# question = [
#     {
#         "question": "What is the capital of France?\nA. Berlin\nB. paris\nC. Rome\nD. Madrid",
#         "answer": "B"
#     },
#
#     {
#         "question": "Which planet is known as the Red Planet\nA.Earth\nB.Venues\nC.Jupiter\nD.Mars",
#         "answer": "D"
#     }
# ]
# for i, item in enumerate(question, start=1):
#     print(f"{i},{item['question']}\n")
#     user_input = input('Enter Your answer: ')
#     if user_input == item['answer'].lower():
#         print("Correct!")
#         score += 1
#     else:
#         print("Incorrect!, going to the next question")
# print("Quiz complete")
# print(f"Your score is: {score} of {len(question)}")

# while True:
#     quiz_question = [
#     {
#         "Question":"What is the capital of Japan?\nA.Seoul\nB.Tokyo\nC.Beijing\nD.Bangkok",
#         "answer": "B"
#     },
#     {
#         "Question":"Who wrote 'Romeo and Juliet'?\nA.Mark Twain\nB.Charles Dickens\nC.William Shakespeare\nD.Jk Rowling",
#         "answer": "C"
#     },
#
#     {
#         "Question":"What is the chemical symbol of water?\nA.H2O\nB.CO2\nC.O2\nD.HO",
#         "answer": "A"
#     },
#
#     {
#         "Question": "How many continents are there?\nA.5\nB.8\nC.7\nD.6",
#         "answer": "C"
#     },
#
#     {
#         "Question": "What is the largest planet in our solar system?\nA.Earth\nB.Saturn\nC.Jupiter\nD.Mars",
#         "answer": "C"
#     }
#
#     ]
#     a = 0
#     for i, question in enumerate(quiz_question, start=1):
#         print(f"{i}.{question['Question']}")
#         user_input = input("Enter your answer: ")
#
#         if user_input == question['answer'].lower():
#             print("correct!")
#             a += 1
#         else:
#             print("Your answer is incorrect!")
#             continue
#
#     user_input_2 = input("Do you need to start from over?(yes/no)")
#     if user_input_2 == "yes":
#       continue
#     else:
#       print("Exiting...")
#       print(f"Your score: {a} out of {len(quiz_question)}")
#       break

users = {"Manu": 560, "Ram": 576, "Jason": 450, "Rahul": 370, "Afam": 200000, "Messi": 900, "Rohit": 890}
print("Welcome To Banking System.")
print("\t")
print("Menu:\n"
      "1.List all users\n"
      "2.Add users\n"
      "3.Delete Users\n"
      "4.Deposit Money\n"
      "5.Withdraw\n"
      "6.Transfer Money\n"
      "7.Get balance\n"
      "8.Exit")


def list_users():
    for key, value in users.items():
        print(f"* {key}: {value}")

def deposit_money():
    deposit_name = input("Enter your name: ")
    is_user_present(deposit_name)
    if deposit_name not in users:
        print(f"{deposit_name} is not found")
    else:
        deposit_amount = int(input("Enter the amount to deposit: "))
        users[deposit_name] += deposit_amount
        print(f"Amount deposited in the {deposit_name} account.")

def is_user_present(user_name):
    return user_name in users

def withdraw_money():
    withdraw_name = input("Enter account name: ")
    if withdraw_name in users:
        withdraw_amount = int(input("Enter the amount you need to withdraw: "))
        if withdraw_amount > users[withdraw_name]:
            print("Your balance is insufficient to transfer!")
        else:
            users[withdraw_name] -= withdraw_amount
            print("Amount has been debited from your account")
    else:
        print(f"{withdraw_name} is not found!")


while True:
    try:
        users_input = int(input("Choose an option: "))
        if users_input == 1:
           list_users()
        elif users_input == 2:
            users_name = input("Enter the name of the user to add: ")
            if users_name in users:
                print(f"{users_name} already exit in the list, please try a different name.")
            users_amount = int(input("Deposit initial payment: "))
            users[users_name] = users_amount
            print("New account created")
            continue
        elif users_input == 3:
            name = input("Enter the name of the user to remove: ")
            if name in users:
                users.pop(name)
                print("User removed")
            else:
                print(f"{name} is not found on the list")

        elif users_input == 4:
            deposit_money()
            is_user_present(users_input)
            # if deposit_name in users:
            # else:
            #     print(f"{deposit_name} is not found")

        elif users_input == 5:
            withdraw_money()

        elif users_input == 6:
            sender_name = input("Enter your account name: ")
            if sender_name not in users:
                print(f"{sender_name} is not found")
                continue
            receiver_name = input("Enter the account name you need to transfer fund: ")
            if receiver_name not in users:
                print(f"{receiver_name} is not found on the list")
                continue
            transfer_amount = int(input("Enter the amount you need to transfer: "))

            if receiver_name in users and sender_name in users:
                users[sender_name] -= transfer_amount
                users[receiver_name] += transfer_amount
                print("Transfer Successful!")
            elif transfer_amount > users[sender_name] or users_input < 0:
                print("Your balance is insufficient")

        elif users_input == 7:
            check_balance = input("Enter account holder name: ")
            if check_balance in users:
                print(f"{check_balance}'s balance is: {users[check_balance]}")
            else:
                print(f"{check_balance} is not found!")
        elif users_input == 8:
            print("Exiting....Thank you for using the banking system")
            break
        else:
            print("you can only enter the number between 1 to 8")

    except ValueError:
        print("Please enter a valid number")