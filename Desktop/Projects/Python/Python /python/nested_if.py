'''
age = int(input("What is your age? "))
if age<=18:
    print("You need to pay 200")
    height = float(input("What is your height in fact? "))
    if height<=3:
        print("you need to pay 200 for the ride")
    elif height>=3:
        print("you need to pay 400")
    else:
        print("pay 500 Rs")
   '''

height = int(input("What is your height in fact? "))
bill = 0
if height>=3:
    print("You can ride")
    age = int(input("What is your age? "))
    if age<12:
        bill = 150
        print("The ticket price is 150 Rs")
    elif age<=18:
        bill = 250
        print("The ticket price is 250 Rs")
    else:
        bill = 500
        print("The ticket price is 500 Rs")

    photos = input("Do you need to take photos? ")
    if photos == 'y' or photos == 'Y':
        bill = bill + 50
        print(f"your total amount is {bill}")

else:
    print("Can't Ride")