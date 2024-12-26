    #print(f"{first_name}, {str_1}")
#greet("Rahul", "How are you doing today")
    #return f"Hi {first_name}, {str_1}"
#print(greet("Rahul","How are you doing today"))
'''
def add(*number):
    a = 0
    for i in number:
        a += i
    return a
print(add(5,6,7,6,9))
'''

'''
def user_detail(**user):
    print(user["phone"])

user_detail(Name="Rahul", Id=45, phone=9037579459)
user_detail(Name="Ramesh", Id=25, phone=995994599)
'''
'''
def fizzbuzz(user):
        if (user) % 3 == 0 and (user) % 5 == 0:
            return "FizzBuzz"
        if user % 3 == 0:
           return "Fizz"
        if user % 5 == 0:
            return "Buzz"
print(fizzbuzz(7))
'''
'''
a = 0
vowel = "aeiou"
user_input = input("Enter a string: ")
for i in user_input:
    if i in vowel:
      a += 1
print(f'The total vowel inside the string is {a}')
'''

'''
def check_even_or_odd():
    user_input = int(input("Enter an number: "))
    for i in range(1,user_input + 1):
        if i % 2 == 0:
            print(f"{i} is an even number")
        else:
            print(f"{i} is an odd number")
check_even_or_odd()
'''
'''def factorial():
    user_input = int(input("Enter a number: "))
    factorial_result = 1
    for i in range(1, (user_input + 1)):
        factorial_result *= i
    print(f"The factorial of {user_input} is {factorial_result}")
factorial()
'''
'''
user_input = int(input("Enter a number: "))

for i in range(2,user_input + 1):
    is_prime = True
    for j in range(2,i):
        if (i % j == 0):
            is_prime = False
            break
    if is_prime:
        print(f"{i} number is Prime number")
    else:
        print(f"{i} number is a constant number")
'''

phone_no = {"Rahul": 9037579459,
            "Ramesh": 9995999459,
            "Afam": 8111899378,
            "Fazil": 9995761061,
            "Sreejith": 3594568811,

            }
'''phone_no["Rahul"] = 9496320858
phone_no["Ramesh"] = {" Business": 9995999459, "Home": 9496320858}
del phone_no["Afam"]
print(phone_no.pop("Ramesh"))
print(phone_no.keys())
print(phone_no.values())    
print(phone_no.items())
print(phone_no)
phone_no_2 = phone_no.copy()
print(phone_no_2)
print(len("Ramesh"))
'''
#phone_no = dict([("Rahul", 9037579459),("Afam", 8111899378),("Fazil", 9995761061),("Sreejith", 3594568811),( "Ramesh", 9995999459)])

#GRADE CONVERTION
'''
student_grade = {"Rahul": 35,
                 "Fazil": 45,
                 "Afam": 95,
                 "Ashif": 17}
student = {}
for i in student_grade:
    mark = student_grade[i]
    if mark > 90:
        student[i] = "A+"
    elif mark > 80:
        student[i] = "A"
    elif mark > 70:
        student_grade[student] = "B+"
    elif mark > 60:
        student[i] = "B"
    elif mark > 50:
        student[i] = "C+"
    elif mark > 40:
        student[i] = "c"
    else:
        student[i] = "F"
print(student)
'''

value = {
    "Rahul": {25},
    "Fazil": {45},
    "Jasim": {67}
}

print(value)