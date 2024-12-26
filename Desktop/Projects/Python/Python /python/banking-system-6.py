print("Welcome To SSIB Bank")

account_holders = {"Rahul": {"password": "724850", "amount": 56000, "privilege": "Admin"},
                   "Afam": {"password": "7485", "amount": 65000, "privilege": "user"},
                   "Fazil": {"password": "6323", "amount": 50000, "privilege": "user"},
                   "jonny": {"password": "2556", "amount": 7500, "privilege": "user"}
                   }
def is_user_found(names):
      if names not in account_holders:
            print("User is not found!")
            return False
      return True

def privilege_check(user_name,is_privilege):
      if is_privilege[user_name]["privilege"] == "Admin":
            return True
      print("You don't have privilege to access this option!")
      return False
def user_list(user_name):
      if privilege_check(user_name,account_holders):
            for index, (name,money) in enumerate(account_holders.items(), start=1):
                  print(f"{index}.{name}:{money['amount']}")

def check_balance(user_name):
      print(f"You account balance is: {account_holders[user_name]['amount']}")

def withdraw_money(user_name,amount):
      if amount > account_holders[user_name]["amount"]:
            return False
      account_holders[user_name]["amount"] -= amount
      print(f"Amount has been withdrawn successfully from {user_name}'s account.")
      return True
def deposit_money(user_name,amount):
      account_holders[user_name]["amount"] += amount
      print(f"Amount has been deposited successfully to {user_name}'s account.")
      return

def transfer_money(user_name):
      username = input("Enter the name of the receiver: ")
      if is_user_found(username):
            amounts = int(input("Enter the amount: "))

            if withdraw_money(user_name, amounts):
                  deposit_money(user_name, amounts)
            else:
                  print("Transfer failed, due insufficient fund!!")
def add_user(user_name):
      if privilege_check(user_name,account_holders):
            add_name = input("Enter the name of the user: ")
            if add_name in account_holders:
                  print("The username already exist in the account, please try with different name.")
                  return
            user_amount = int(input("initial payment minimum 5000 or above:  "))
            if user_amount < 5000:
                  print("Amount Should be deposited minimum 5000.")
                  return
            user_password = input("Create a password: ")
            account_holders[add_name] = {
                  "password": user_password,
                  "amount": user_amount,
                  "privilege": "user"
            }
            print("User added successfully!!")

def remove_user(user_name):
      if privilege_check(user_name,account_holders):
            delete_user = input("Enter the name the user to remove: ")
            if is_user_found(delete_user):
                  account_holders.pop(delete_user)
                  print("User has been removed successfully!!")
def user_option():
      while True:
            print("1.Login\n2.Exit")
            user = int(input("Please enter the option: "))

            if user == 1:
                  user_name = input("Username: ")
                  password = input("Password: ")

                  if user_name not in account_holders or account_holders[user_name]["password"] != password:
                        print("incorrect username or password!")
                        continue

                  while True:
                        try:
                              print("Menu:"
                                    "\n(1)USER LIST\n(2)CHECK BALANCE\n(3)DEPOSIT\n(4)WITHDRAW\n(5)TRANSFER\n(6)ADD USER\n(7)REMOVE USER\n(8)LOGOUT")
                              user_choice = int(input("Enter your choice: "))

                              if user_choice == 1:
                                    user_list(user_name)
                                    continue

                              elif user_choice == 2:
                                    check_balance(user_name)

                              elif user_choice == 3:
                                    amount = int(input("Enter the amount: "))
                                    deposit_money(user_name, amount)

                              elif user_choice == 4:
                                    amount = int(input("Enter the amount: "))
                                    withdraw_money(user_name, amount)

                              elif user_choice == 5:
                                    transfer_money(user_name)

                              elif user_choice == 6:
                                    add_user(user_name)

                              elif user_choice == 7:
                                    remove_user(user_name)

                              elif user_choice == 8:
                                    print("logout successfully!!")
                                    break
                              else:
                                    print("Please enter a valid input!!")

                        except ValueError:
                              print("Enter a valid input!")

            if user == 2:
                  print("Program Exit...")
                  exit()
user_option()