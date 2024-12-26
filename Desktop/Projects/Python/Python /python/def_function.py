# def calculater():
#     num1 = int(input("Enter the 1st number: "))
#     num2 = int(input("Enter the 2nd number: "))
#     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
#     choice = int(input("Enter your choice:"))
#     if choice == 1:
#         result = num1 + num2
#     elif choice == 2:
#         result = num1 - num2
#     elif choice == 3:
#         result = num1 * num2
#     elif choice == 4:
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             return "You can't divide a number by zero"
#     else:
#         return "Choose an option that has provided on the screen"
#     return f"The total after adding both number = {result}"

# print("big" > "small")
# number = 4
# if number * 4 < 15:
#  print(number / 4)
# elif number < 5:
#  print(number + 3)
# else:
#  print(number * 2 % 5)

# test_num = 12
# if test_num > 15:
#     print(test_num / 4)
# else:
#     print(test_num + 3)

# def calculator():
#     while True:
#         num_1 = int(input('Enter first number: '))
#         while True:
#             print("+\n-\n*\n/\n")
#             operation = input("Pick an operation: ")
#             num_2 = int(input("Enter second number: "))
#             if operation == "+":
#                 result = num_1 + num_2
#                 print(f"{num_1} + {num_2} = {result}")
#             elif operation == "-":
#                 result = num_1 - num_2
#                 print(f"{num_1} + {num_2} = {result}")
#             elif operation == "*":
#                 result = num_1 * num_2
#                 print(f"{num_1} + {num_2} = {result}")
#             elif operation == "/":
#                 result = num_1 / num_2
#                 print(f"{num_1} + {num_2} = {result}")
#             else:
#                 print("Enter a valid operation")
#                 continue
#             user_input = input(f"Enter 'Y' to continue with the calculation of {result} or 'n' to start new calculation or 'X' to exit: ")
#             if user_input == 'y':
#                 num_1 = result
#             elif user_input == "n":
#                 break
#             elif user_input == "x":
#                 print("Exciting the calculator, good bye!")
#                 return
# calculator()

# def function(num1,num2):
#     return num1 + num2
# print(123)
# print('abc')
# total = function(55,66)
# print(total)

# list1 = []
# def sum_of_list_numbers(numbers):
#     return sum(int(num) for num in numbers)
# while True:
#     user_number = input("Enter a number: ")
#     if user_number == 'q':
#         print("Exiting....")
#         break
#     else:
#         list1.append(user_number)
#
# print(sum_of_list_numbers(list1))

def sum_list_numbers():
    num = [1, 3, 6, 7, 9, 7]
    return sum(num)
total = sum_list_numbers()
print(f"The sum of list: {total}")