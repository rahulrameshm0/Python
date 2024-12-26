class Banking:
    user_list = {"Afam":6500, "Rahul": 4500}

    def __init__(self):
        pass

    def withdraw(self):
        try:
            withdraw_name = input("Enter the name: ")
            if withdraw_name not in self.user_list:
                print("User is not found!!")
                return False

            amount = int(input("Enter a amount: "))
            if amount > self.user_list[withdraw_name]:
                print("Balance is insufficient!!")
                return False

            self.user_list[withdraw_name] -= amount
            print('Amount withdrawn successfully!!')
            return True

        except ValueError:
            print("Please enter a valid input!")
            return False

    def deposit(self):
        try:
            user_name = input("Enter your name: ")
            if user_name not in self.user_list:
                print("User is not found!!")
                return False

            amount = int(input('Enter the amount: '))
            self.user_list[user_name] += amount
            print("deposit successful!!")
            return True

        except ValueError:
            print("Please enter a valid input!!")
            return False
banking_system = Banking()
print(banking_system.deposit())
print(banking_system.withdraw())


