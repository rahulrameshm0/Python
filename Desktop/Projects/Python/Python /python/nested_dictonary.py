# student_data = {
#     "Rahul": {"Age": 25, "Roll No": 10, "Course": "Python"},
#     "Ashif": {"Age": 23, "Roll No": 8, "Profession": "Fitness Trainer"},
#     "Afam": {"Age": 26, "Roll No": 20, "Profession": "Computer Engineer"},
#     "Sreejith": {"Age": 26, "Roll No": 11, "Profession": "Hacker"}
# }
#print(student_data["Rahul"])
#print(student_data["Rahul"]["Course"])
# student_data["Rahul"]["Phone_no"] = 5598485236, 3496320858
# print(student_data["Rahul"])
# print(student_data["Rahul"].pop("Phone_no"))
# print(student_data["Rahul"])

#Nesting a list in the witin the dictonary
# states = {
#     "Kerala": ["Kochi","Mallapuram","Calicut","Waynad"]
# }
# print(states)

#List within a dictonary

# student_data = [
#             {
#                 "Name": "Rahul",
#                 "Age": 25,
#                 "Roll No": 10,
#                 "Course": "Python"
#             },
#
#             {
#                 "Name": "Ashif",
#                 "Age": 23,
#                 "Roll No": 8,
#                 "Profession": "Fitness Trainer"
#              },
#
#             {
#                 "Name": "Afam",
#                 "Age": 26,
#                 "Roll No": 20,
#                 "Profession": "Computer Engineer"},
#
#             {
#                 "Name": "Sreejith",
#                 "Age": 26,
#                 "Roll No": 11,
#                 "Profession": "Hacker"
#             }
#         ]
# print(student_data[3]["Profession"])

# student_data = [
#
#              {
#                  "Name": "Rahul",
#                  "Age": 25,
#                  "Roll No": 10,
#                  "Course": "Python"
#              },
#
#              {
#                  "Name": "Ashif",
#                  "Age": 23,
#                  "Roll No": 8,
#                  "Profession": "Fitness Trainer"
#               },
#
#              {
#                  "Name": "Afam",
#                  "Age": 26,
#                  "Roll No": 20,
#                  "Profession": "Computer Engineer"
#              },
#
#              {
#                  "Name": "Sreejith",
#                  "Age": 26,
#                  "Roll No": 11,
#                  "Profession": "Hacker"
#              }
#          ]

# def add_new_student(Name, Age, Roll, profession):
#     new_student = {}
#     new_student["Name"] = "Fazil"
#     new_student["Age"] = 25
#     new_student["Roll_no"] = 15
#     new_student["Course"] = "C++"
#     student_data.append(new_student)
# add_new_student(Name="Fazil",Age=25,Roll=15,profession= "C++")
# print(student_data)
import os
import time
import subprocess
# import os
# dict_1 = {}
# while True:
#     name = input("Enter your name: ")
#     bid = int(input("Enter your bid: "))
#     member = input("Is there any other bidders? type Yes/No: ")
#     dict_1[name] = bid
#     if member == "NO" or member == "no":
#         break
#     os.system('clear')
# highest_bidder = max(dict_1, key=dict_1.get)
# print(f"Here is the list of all the Bidders: {dict_1}")
# print(f"The winner is {highest_bidder} with the bid of {dict_1[highest_bidder]}")


