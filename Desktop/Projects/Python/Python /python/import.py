# import random
#
#
# print("Guess a number between 1 to 10")
#
# while True:
#     num1 = int(input("Enter a number between 1 to 10: "))
#     guess = random.randint(1, 30)
#     if num1 == guess:
#         print("Your number is correct!")
#         break
#     else:
#         print(f"Wrong guessing, actual number was: {guess}")
#         continue

def importer():
    from library_management_2 import library_books
importer()