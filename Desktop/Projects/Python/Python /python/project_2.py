import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!', '@', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to password generator!")

n_letters = int(input("How many letters do you need in your password?\n"))
n_numbers = int(input("How many numbers do you need in your password?\n"))
n_symbols = int(input("How many symbols do you need in your password?\n"))
password_list = []
for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_list.append(char)

for i in range(1, n_numbers + 1):
    char = random.choice(numbers)
    password_list.append(str(char))

for i in range(1, n_symbols + 1):
    char = random.choice(symbols)
    password_list.append(char)
print(password_list)

random.shuffle(password_list)
print(password_list)
password = ''
for char in password_list:
    password = password + char
print(password)