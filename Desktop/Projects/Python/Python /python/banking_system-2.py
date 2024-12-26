# a = 0
# b = 0
# user1 = int(input("Enter 1st number: "))
# a = a + user1
# user2 = int(input("Enter 2nd number: "))
# b = b + user2
#
# def add(a,b):
#     return a + b
# result = add(a,b)
# print(result)
#
# def multiplication(num1,num2):
#

# Get user inputs
print("Welcome To Banking System")
print("1.List all user"
      "\n2.Add Users"
      "\n3.Delete User"
      "\n4.Deposit Money"
      "\n5.Withdraw Money"
      "\n6.Transfer Money"
      "\n7.Get Balance"
      "\n8.Exit"
      )

users_list = {}

def list_of_users():
    if not users_list:
        print("Account Empty!!")
    for key, value in users_list.items():
        print(f"* {key}: {value}")

def add_user():
    add_name = input("Enter Your Name: ")
    add_amount = int(input("Enter deposit Amount: "))
    users_list[add_name] = add_amount
    return "New User added successfully!!"

def delete_user():
    remove_user = input("Enter the name of the user to remove: ")
    if not users_list:
        print("User is not found!!")
    users_list.pop(remove_user)
    print(f"{remove_user} has been removed successfully!!")

def deposit_amount():
    deposit_name = input("Enter the name of the depositer: ")
    if not users_list:
        print(f"There is no name called {deposit_name} on the list")
    elif deposit_name in users_list:
        add_amount = int(input("Enter the amount to deposit: "))
        users_list[deposit_name] = users_list[deposit_name] + add_amount

    option = input("Do you need to transfer the fund (yes/no)?: ")
    if option == "yes":
        receiver_name = input("Enter the name of receiver: ")
        receiver_amount = int(input("Enter the amount: "))
        transfer_amount(deposit_name, receiver_name, receiver_amount)
        print("Transfer Successful!!")
    else:
        print(f"Amount deposit successfully to {deposit_name} account!")

def withdraw_amount():
    withdrawing_name = input("Enter the name of the withdrawing person: ")
    if not users_list:
        print("The user is not found!!")
    elif withdrawing_name in users_list:
        withdrawing_amount = int(input("Enter the amount you need to withdraw: "))
        users_list[withdrawing_name] = users_list[withdrawing_name] - withdrawing_amount
        option_2 = input("Do you need to transfer the fund? (yes/no): ")
        if option_2 == "yes":
            receiver_name = input("Enter the name of the receiver: ")
            money = int(input("Enter the amount you need to transfer: "))
            if not users_list:
                print("User is not found")
            transfer_amount(withdrawing_name, receiver_name, money)
        else:
            print("Amount has been withdrawn successfully!!")

def transfer_amount(sender_name, receiver_name,fund_transfer):

    if users_list[sender_name] < fund_transfer:
        print("Balance is insufficient")
        return

    if sender_name and receiver_name in users_list:
        users_list[sender_name] -= fund_transfer
        users_list[receiver_name] += fund_transfer
        print("Transfer Successful!!")


def get_balance():
    user_name = input("Enter the name of the user to check the balance: ")
    if not users_list:
        print(f"{user_name} is not found!!")
    print(f"Balance: {users_list[user_name]}")


while True:
    try:
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            list_of_users()
        elif choice == 2:
           add_user()
        elif choice == 3:
            delete_user()
        elif choice == 4:
            deposit_amount()
        elif choice == 5:
            withdraw_amount()
        elif choice == 6:
            sender_name = input("Enter your name (sender): ")
            if sender_name not in users_list:
                print("User is not found!!")
                continue
            receiver_name = input("Enter the receiver's name: ")
            if receiver_name not in users_list:
                print("User is not found")
                continue
            fund_transfer = int(input("Enter the amount to transfer: "))
            transfer_amount(sender_name, receiver_name, fund_transfer)
        elif choice == 7:
            get_balance()
        elif choice == 8:
            print("Program Exiting...")
            break
        else:
            print("You can only enter the number b/w 1 to 8")

    except ValueError:
        print("Please Enter a valid number!!")
