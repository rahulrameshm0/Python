user = int(input("Enter a number: "))
is_prime = True
for i in range(2, user):
    if user % i == 0:
        is_prime = False
if is_prime:
    print(f"{user} is a prime number: ")
else:
    print(f"{user} is not a prime number")
