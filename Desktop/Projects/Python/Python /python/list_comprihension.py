# names = [("Rahul", 25), ("Ramesh", 53), ("Rohit", 18), ("Binsy", 53), ("Jasim", 53), ("Afam", 23), ("Sonny", 15)]
#
# list2 = [names for (names,age) in names if age >= 53]
# print(f"{list2}")

# values = []
# for i in range(10):
#     values.append(i)
#
# values = [i + 1 for i in range(10)]
#
# print(values)

# evens = []
# for number in range(20):
#     if number % 2 == 0:
#         evens.append(number)
#
# print(evans)

#
# evens = []
#
# for number in range(50):
#     if number % 2 == 0:
#         evens.append(number)
#
# evens = [number + 2 for number in range(50) if number % 2 == 0]
#
# print(evens)

option = ['jason', 'jonny', 'mans', 'adas']
valid = []

for strings in option:
    if len(strings) <= 1:
        continue
    if strings[0] != 'a':
        continue
    if strings[-1] != 's':
        continue
    valid.append(strings)

print(strings)




