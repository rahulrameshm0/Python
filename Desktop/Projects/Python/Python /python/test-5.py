a = 1
count = 0
user = int(input("Enter a number: "))
while a <= user:
    if a % 2 == 0:
        count = count + a * a
    a = a + 1
print(f"The sum of even number is: {count}")