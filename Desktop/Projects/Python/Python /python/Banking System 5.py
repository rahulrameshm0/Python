print("Welcome To SSIB Bank")

account_holders = {"Rahul": {
                        "password": "724850",
                        "amount": 56000,
                        "privilege": "Admin"},

                  "Afam":{
                        "password": "7485",
                        "amount": 65000,
                        "privilege": "user"
                   },

                   "Fazil":{
                        "password": "6323",
                        "amount": 50000,
                        "privilege": "user"
                   },

                   "jonny":{
                         "password": "2556",
                         "amount": 7500,
                         "privilege": "user"
                   }
            }

def is_user_found(names):
      if names not in account_holders:
            print("User is not found!")
            return False
      return True
def user_list():
      for index, (name,money) in enumerate(account_holders.items(), start=1):
            print(f"{index}.{name}:{money['amount']}")

def check_balance():
      name = input("Enter the name of the account holder: ")
      if is_user_found(name):
            print(f"You account balance is: {account_holders[name]["amount"]}")

def deposit_money(receiver,amount):
      if is_user_found(receiver):
            account_holders[receiver]["amount"] += amount
            print(f"Amount has been deposited successfully to {receiver}'s account.")
def withdraw_money(sender,amount):
      if is_user_found(sender):
            account_holders[sender]["amount"] -= amount
            print(f"Amount has been withdrawn successfully from {sender}'s account.")

def transfer_money():
      transfer_name = input("Enter your name: ")
      if is_user_found(transfer_name):
            receiver_name = input("Enter the name of the receiver: ")
            if is_user_found(receiver_name):
                  amounts = int(input("Enter the amount: "))
                  if amounts > account_holders[transfer_name]["amount"]:
                        print("Insufficient Balance!!")
                        return
                  deposit_money(receiver_name,amounts)
                  withdraw_money(transfer_name,amounts)

def add_user():
      user_name = input("Enter the name of the user: ")
      if user_name in account_holders:
            print("The username already exist in the account, please try with different name.")
            return
      user_amount = int(input("initial payment minimum 5000 or above:  "))
      if user_amount < 5000:
            print("Amount Should be deposited minimum 5000.")
            return
      user_password = input("Create a password: ")
      account_holders[user_name] = {
            "password":user_password,
            "amount": user_amount,
            "privilege":"user"
      }
      print("User added successfully!!")

def remove_user():
      delete_user = input("Enter the name the user to remove: ")
      if is_user_found(delete_user):
            account_holders.pop(delete_user)
            print("User has been removed successfully!!")

user_name = input("Enter your name: ")
password = input("Enter your password: ")
if user_name not in account_holders or account_holders[user_name]["password"] != password:
      print("incorrect username or password!")
else:
      print("Menu:"
            "\n1.User List"
            "\n2.Check Balance"
            "\n3.Deposit"
            "\n4.Withdraw"
            "\n5.Transfer"
            "\n6.Add user"
            "\n7.Remove User"
            "\n8.Exit")

      while True:
            try:
                  user_choice = int(input("Enter your choice: "))
                  if user_choice == 1:
                        if account_holders[user_name]["privilege"] == "Admin":
                              user_list()
                        else:
                              print("You don't have privilege to access this option!")
                              continue

                  elif user_choice == 2:
                        check_balance()

                  elif user_choice == 3:
                        deposit_name = input("Enter the name of the depositer: ")
                        if is_user_found(deposit_name):
                              money = int(input("Enter the amount you need to deposit: "))
                              deposit_money(deposit_name,money)

                  elif user_choice == 4:
                        holder_name = input("Enter the name of the user: ")
                        if is_user_found(holder_name):
                              amount = int(input("Enter the amount: "))
                              # if amount > account_holders[holder_name]["amount"]:
                              #       print("Balance is insufficient")
                              #       continue
                              withdraw_money(holder_name,amount)

                  elif user_choice == 5:
                        transfer_money()

                  elif user_choice == 6:
                        if account_holders[user_name]["privilege"] == "Admin":
                              add_user()
                        else:
                              print("You don't have privilege to access this option!!")

                  elif user_choice == 7:
                        if account_holders[user_name]["privilege"] == " Admin":
                              remove_user()
                        else:
                              print("You don't have privilege to access this option!!")

                  elif user_choice == 8:
                        print("Thank you using our banking system!!")
                        break

            except ValueError:
                  print("Please enter a valid number!!")