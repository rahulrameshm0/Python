'''
list1 = []
def to_do_list(list_items):
	list1.append(list_items)
	return list1

while True:
	list_name = input("Enter a list of things you need to do or ('done to exit'): ")

	if list_name.lower() == "done":
		break
	to_do_list(list_name)
print("The Items you added to the list:")
for i in list1:
	print(i)
'''

#Budget Trcker



# def budget_tracker(current_budget, amount, operation):
# 	if operation == 1:
# 		return current_budget + amount
# 	elif operation == 2:
# 		return current_budget - amount
# 	else:
# 		return current_budget
#
# budget = 0
#
# while True:
# 	print("1.Add Income\n2.Add Expense\n3.View Budget\n4.Exit")
# 	try:
# 		user_choice = int(input("Enter your choice: "))
# 		if user_choice == 1:
# 			add_money = int(input("Add amount: "))
# 			budget = budget_tracker(budget,add_money,1)
# 			print(f"Income added, your current budget is: {budget}")
# 		elif user_choice == 2:
# 			user_expense = int(input("Enter your expense: "))
# 			if user_expense > budget:
# 				print("You don't have enough amount")
# 			else:
# 				#budget -= user_expense
# 				budget = budget_tracker(budget, user_expense, 2)
# 				print(f"Expense added, your current budget is: {budget}")
# 		elif user_choice == 3:
# 			print(f"Your current budget is {budget}")
# 		elif user_choice == 4:
# 			print("Exiting...Thank you for using budget tracking!")
# 			break
# 		else:
# 			print("The choice you are entering should be 1 to 4")
# 	except ValueError:
# 		print("please enter a valid option!")


# print('Welcome to the basic banking system!\n')
# print("1.Check balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")
# def banking_system(current_balance, deposit_amount, operation):
#     if operation == 2:
#         return current_balance + deposit_amount
#     elif operation == 3:
#         return current_balance - deposit_amount
#     else:
#         return current_balance
# balance = 0
# while True:
#     try:
#         user_choice = int(input("Enter your choice: "))
#         if user_choice == 1:
#             print(f"Your current balance is {balance}")
#         elif user_choice == 2:
#             user_deposit_money = int(input("Enter the amount to deposit: "))
#             balance = banking_system(balance, user_deposit_money, 2)
#             print(f"Deposit successful! your current deposit amount is: {balance}")
#         elif user_choice == 3:
#             user_withdraw_money = int(input("Enter the amount you need to withdraw: "))
#             if user_withdraw_money < balance:
#                 balance = banking_system(balance, user_withdraw_money,3)
#             else:
#                 print("Yor balance is insufficient!")
#         elif user_choice == 4:
#             break
#     except ValueError:
#         print("Please enter a valid number!")