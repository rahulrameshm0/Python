'''
number = 1
while number <=10:
    print(number)
    number = number + 1
    if number == 7:
     break
print("out of loop")
'''

'''
list = ["Hi","hello","welcome"]
names = ["Ashique","Afam","Warner"]
for item in list:
    for name in names:
        print(item,name)
        if item == "hello" and name == "Afam":
            break
    print("out from inner loop")
print("out from outer loop")
'''

'''
number = 0
while number <= 10:
    number = number + 1
    if number == 5:
        continue
    print(number)
print("out of loop")
'''
number = 0
while number <= 10:
    number = number + 1
    if number == 5:
        pass
    print(number)
print("out of loop")