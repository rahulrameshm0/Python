'''def add(*numbers):
    a = 0
    for i in numbers:
        a = a + i
    print(f"Total is = {a}")
add(5, 7, 8, 9, 1, 10)
add(25,25)
add(25, 35, 45, 15)
'''

'''
def multiply(*numbers):
    a = 1
    for i in numbers:
        a = a * i
    print(f"Total = {a}")
multiply(2, 3, -6, 8)
multiply(2, 5, -6, 8, 9)
'''
'''import math
def paint(height, width, coverage):
    a = int(input("Enter the height of the wall in meter:\n"))
    b = int(input("Enter the width of the wall in meter:\n"))
    cover = 7
    area = a * b / cover
    print(f"you will need {math.ceil(area)} cans of paint")
paint(height=0,width=0, coverage =0)
'''

# def prime(number):
#     user_input = int(input("Enter a number: "))
#     is_prime = True
#     for i in range(2,number):
#         is_prime = False
#         if i % 2 == 0:
#             print(f"{user_input} is a prime number")
#     else:
#         print(f"{user_input} is not a prime number")
# prime(0)
