'''
name = len("Rahul Ramesh")
print("Your length of the characters is " + str(name))
print(type(name))
'''

#int()
#float()
#str()

# num_1 = input("Enter first number: ")
# num_2 = input("Enter second number: ")
# sum = int(num_1) + int(num_2)
#
# print("Result = ",sum)


# mydict = {"Name": "Rahul", "Age": 26, "Contact": 9496320858}
#
# for x in mydict.keys():
#     for i in mydict.values():
#         print(x)
#     print(i)


a = 1
user_input = int(input("Enter a number: "))

for i in range(1, user_input + 1):
    a = a * i
print(a)
