try:
    a = int(input("Enter a number: "))
    while True:
        user = int(input("Enter a number: "))
        if a == user:
            print("Program Exit...")
            break
        a = user
except ValueError:
    print("Please enter a valid number")