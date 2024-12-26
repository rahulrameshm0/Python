# data = [
#     {
#         "Name": "Rahul",
#         "Follower_count": 1,
#         "Description": "Software Engineer",
#         "Country": "India"
#     },
# {
#         "Name": "Messi",
#         "Follower_count": 655,
#         "Description": "Atle",
#         "Country": "Argentina"
#     },
# {
#         "Name": "Dhoni",
#         "Follower_count": 1,
#         "Description": "Cricketer",
#         "Country": "India"
#     },
# {
#         "Name": "Rodri",
#         "Follower_count": 65,
#         "Description": "Footballer",
#         "Country": "Spain"
#     },
# {
#         "Name": "Ronaldo",
#         "Follower_count": 755,
#         "Description": "Footballer",
#         "Country": "Portugal"
#     },
# {
#         "Name": "Kohli",
#         "Follower_count": 455,
#         "Description": "Cricketer",
#         "Country": "India"
#     },
# {
#         "Name": "Justin",
#         "Follower_count": 600,
#         "Description": "Artist",
#         "Country": "Canada"
#     },
# {
#         "Name": "Fazil",
#         "Follower_count": 423,
#         "Description": "You Tuber",
#         "Country": "India"
#     },
# {
#         "Name": "Narendra Modi",
#         "Follower_count": 75,
#         "Description": "Prime Minister",
#         "Country": "India"
#     },
# {
#         "Name": "Afam",
#         "Follower_count": 98,
#         "Description": "Software Engineer",
#         "Country": "India"
#     },
# {
#         "Name": "Sreejith",
#         "Follower_count": 89,
#         "Description": "Software Engineer",
#         "Country": "India"
#     },
# {
#         "Name": "Salena Gomez",
#         "Follower_count": 755,
#         "Description": "Artist",
#         "Country": "I
#
# even = 0
# odd = 0
# while True:
#     user = input("Enter a number: ")
#     if user == "q":
#         print("Program Exiting....")
#         break
#     user = int(user)
#     if user % 2 == 0:
#         even = even + user
#     else:
#         odd = odd + user
# print(f"Total of even number = {even}")
# print(f"Total of odd number = {odd}")


#         return (f"Total = {a}")
# result = add()
# print(result)

# count = 0
# a = 1
# user = int(input("Enter a number: "))
# while a <= user:
#     count = count + a * a
#     a = a + 1
# print(f"Total = {count}")

odd = 0
even = 0
i = 1
n = 0
a = 0

while i <= 10:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        even = even + number
    else:
        odd = odd + number
    i = i + 1
print("Total od Odd = ", odd)
print("Total of even = ", even)