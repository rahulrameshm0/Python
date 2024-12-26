print("Welcome to Banking System!")

account_holders = {"Afam":25000, "Rahul":5600, "Sonny":56000}

print("Menu:"
      "\n1.User List"
      "\n2.Check Balance"
      "\n3.Deposit"
      "\n4.Withdraw"
      "\n5.Transfer"
      "\n6.Add user"
      "\n7.Remove User"
      "\n8.Exit")

def is_user_found(names):
      if names not in account_holders:
            print("User is not found!")
            return False
      return True
def user_list():
      for index, (name,money) in enumerate(account_holders.items(), start=1):
            print(f"{index}.{name}: {money}")

def check_balance():
      name = input("Enter the name of the account holder: ")
      if is_user_found(name):
            print(f"Your balance is {account_holders[name]}")

def deposit_money(receiver,amount):
      if is_user_found(receiver):
            account_holders[receiver] += amount
            print(f"Amount has been deposited successfully form {receiver}'s account.")
def withdraw_money(sender,amount):
      if is_user_found(sender):
            account_holders[sender] -= amount
            print(f"Amount has been withdrawn successfully from {sender}'s account.")

def transfer_money():
      transfer_name = input("Enter your name: ")
      if is_user_found(transfer_name):
            receiver_name = input("Enter the name of the receiver: ")
            if is_user_found(receiver_name):
                  amounts = int(input("Enter the amount: "))
                  if amounts > account_holders[transfer_name] :
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
      account_holders[user_name] = user_amount
      print("User added successfully!!")

def remove_user():
      delete_user = input("Enter the name the user to remove: ")
      if is_user_found(delete_user):
            account_holders.pop(delete_user)
            print("User has been removed successfully!!")


while True:
      try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                  user_list()

            elif user_choice == 2:
                  check_balance()

            elif user_choice == 3:
                  deposit_name = input("Enter the name of the depositer: ")
                  if is_user_found(deposit_name):
                        money = int(input("Enter the amount you need to deposit: "))
                        print("deposit successfully!!")
                        deposit_money(deposit_name,money)

            elif user_choice == 4:
                  holder_name = input("Enter the name of the user: ")
                  if is_user_found(holder_name):
                        amount = int(input("Enter the amount: "))
                        if amount > account_holders[holder_name]:
                              print("Balance is insufficient")
                              continue
                        withdraw_money(holder_name,amount)
                        print("Withdraw Successful!")

            elif user_choice == 5:
                  transfer_money()

            elif user_choice == 6:
                  add_user()

            elif user_choice == 7:
                  remove_user()

            elif user_choice == 8:
                  print("Thank you using our banking system!!")
                  break

      except ValueError:
            print("Please enter a valid number!!")
