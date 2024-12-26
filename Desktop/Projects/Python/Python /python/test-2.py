d = 0
count = 0
user = int(input("Enter number: "))
while user > 0:
    d = user % 10
    count = count + d
    user = user / 10
print(round(count))
