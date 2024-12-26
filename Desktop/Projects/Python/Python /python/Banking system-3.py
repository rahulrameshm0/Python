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

users_list = {"Rahul": 2500,
              "Afam": 5220,
              "Sonny": 25000}
def list_of_users():
    if not users_list:
        print("Account Empty!!")
    for index, (user, balance) in enumerate(users_list.items(), start=1):
        print(f"{index}. {user}: {balance}")


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

def deposit_amount(receiver,amount):
    if not users_list:
        print(f"There is no name called {receiver} on the list")
    elif receiver in users_list:
        users_list[receiver] = users_list[receiver] + amount
        print(f"Amount deposit successfully to {receiver} account!")

def withdraw_amount(sender,amount):
    if sender in users_list:
        if amount > users_list[sender]:
            print("Balance in insufficient!")
            return
        users_list[sender] = users_list[sender] - amount
        print("Amount has been withdrawn successfully!!")
    else:
        print(f"{sender} is not found!")

def transfer_amount():
    sender_name = input("Enter your name: ")
    if sender_name not in users_list:
        print("user is not found!!!")
        return
    receiver_name = input("Enter receiver name: ")
    if receiver_name not in users_list:
        print("user is not found")
        return
    amounts = int(input("Enter the amount: "))
    if amounts > users_list[sender_name]:
        print("Your account balance is insufficient!!")
        return
    withdraw_amount(sender_name, amounts)
    deposit_amount(receiver_name,amounts)

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
            deposit_name = input("Enter depositer name: ")
            if deposit_name not in users_list:
                print(f"{deposit_name} is not found!!")
                continue
            amount = int(input("Enter the amount to deposit: "))
            deposit_amount(deposit_name,amount)
        elif choice == 5:
            sender_name = input("Enter your name: ")
            if sender_name not in users_list:
                print("User is not found!!")
                continue
            amount = int(input("Enter the amount to withdraw: "))
            withdraw_amount(sender_name, amount)
        elif choice == 6:
            transfer_amount()
        elif choice == 7:
            get_balance()
        elif choice == 8:
            print("Program Exiting...")
            break
        else:
            print("You can only enter the number b/w 1 to 8")

    except ValueError:
        print("Please Enter a valid number!!")