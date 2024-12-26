
count1 = 0
count2 = 0
user = int(input("Enter a number: "))
for i in range(1,user + 1):
    if i % 3 == 0:
        count1 = count1 + 1
    elif i % 5 == 0:
        count2 = count2 + 1
print(f"3 is divisible {count1} times")
print(f"5 is divisible {count2} times")
