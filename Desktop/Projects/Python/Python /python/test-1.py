user = int(input("Enter a number: "))
a = 0
b = 1
count = 0
while count < user:
    print(a, end="\t")
    a,b = b,  a + b
    count = count + 1
