print("Welcome to SSIB Bank")
class Banking_System:

    account_holders = {
        "Afam": {"amount": 25000, "password": "7485", "privilege": "user"},

        "Rahul": {"amount": 5600, "password": "7248", "privilege": "Admin"},

        "Sonny": {"amount": 6000, "password": "8563", "privilege": "user"}
    }

    def __init__(self):
        pass

    def is_user_found(self,names):
        if names not in self.account_holders:
            print("User is not found!!")
            return False
        return True

    def user_list(self):
        for index, (name,money) in enumerate(self.account_holders.items(), start=1):
            print(f"{index}.{name}: {money["amount"]}")

    def check_balance(self):
        if self.is_user_found(username):
            print(f"You account balance is: {self.account_holders[username]["amount"]}")

    def deposit_amount(self, username, amount):
        self.account_holders[username]["amount"] += amount
        print(f"Deposited to {username}'s account successfully!!")

    def withdraw_amount(self, username, amount):
        if amount > self.account_holders[username]["amount"]:
            print("Balance is insufficient!!")

        self.account_holders[username]["amount"] -= amount
        print(f"Withdrawn successfully from {username}'s account")
        return

    def transfer_amount(self):
            receiver_name = input('Enter the name of the receiver: ')
            if self.is_user_found(receiver_name):
                money = int(input("Enter the amount you need to transfer: "))
                self.account_holders[username]["amount"] -= money

                self.deposit_amount(receiver_name, money)
                self.withdraw_amount(username, money)

    def add_user(self):
        user_name = input("Enter your name to create a new account: ")
        if user_name not in self.account_holders:
            password = input("enter your password to log in: ")
            initial_payment = int(input("Enter the initial payment, minimum 5000: "))
            if initial_payment < 5000:
                print("The amount should be minimum 5000!!")
                return
            self.account_holders[user_name] = {"amount": initial_payment, "password": password, "privilege": "user"}
            print("User added successfully!!")
            return

        print("This name is already exsited in the bank account, please try with a different name!!")

    def delete_user(self):
        delete_account = (input("Enter the name of the user: "))
        if self.is_user_found(delete_account):
            self.account_holders.pop(delete_account)

    def verify_login(self,username, code):
        if username in self.account_holders:
            if self.account_holders[username]["password"] == code:
                return True
        return False

banking = Banking_System()
print("1.login\n2.Exit")
try:
    chose_option = int(input("choose an option: "))
    if chose_option == 1:
        username = input("Enter username: ")
        code = input("Enter the password: ")

        if banking.verify_login(username,code):
            print(f"Welcome {username}")

            while True:
                print("Menu:\n1.User List\n2.Check Balance\n3.Deposit\n4.Withdraw\n5.Transfer\n6.Add user\n7.Remove User\n8.Exit\n9.Logout")
                user_choice = int(input("Enter your choice: "))
                if user_choice == 1:
                    if banking.account_holders[username]["privilege"] == "Admin":
                        banking.user_list()
                    else:
                        print("Only admin can access the user list.")

                elif user_choice == 2:
                    banking.check_balance()

                elif user_choice == 3:
                    receiver_amount = int(input("Enter the amount: "))
                    banking.deposit_amount(username, receiver_amount)

                elif user_choice == 4:
                    sender_amount = int(input("Enter the amount: "))
                    banking.withdraw_amount(username, sender_amount)

                elif user_choice == 5:
                    banking.transfer_amount()

                elif user_choice == 6:
                    if banking.account_holders[username]["privilege"] == "Admin":
                        banking.add_user()
                    else:
                        print("Only admin can add account.")

                elif user_choice == 7:
                    if banking.account_holders[username]["privilege"] == "Admin":
                        banking.delete_user()
                    else:
                        print("Only admin can delete the account.")

                elif user_choice == 8:
                    print("program exit..Thank You for using the SSIB bank!!")
                    break

                else:
                    print("Invalid no, please try again!!")

        elif chose_option == 2:
            print("Thank you for using SSIB Bank")
        else:
            print("User name or password incorrect!!")

except ValueError:
    print("Please enter a valid input...")
