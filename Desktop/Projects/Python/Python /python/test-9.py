user1 = int(input("Enter 1st number: "))
user2 = int(input("Enter 2nd number: "))

def add(a,b):
    return a + b

def multiply(a, b):
    result = 0
    for i in range(b):
        result = add(result, a)
    return result
def add_multiply(a, b):
    addition = add(a,b) + multiply(a,b)
    return addition
total = add_multiply(user1, user2)
print(total)