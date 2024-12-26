
'''
n_list = []
while True:
    user_input = (input("Enter a number or q quite: "))
    if user_input == "q":
        print("Program completed")
        break

    user_input = int(user_input)
    if user_input not in n_list:
        n_list.append(user_input)
    else:
        print("You already entered a number, try a different number")
print(f"The number you have entered is = {n_list}")
'''


