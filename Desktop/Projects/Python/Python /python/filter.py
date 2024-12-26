# def grades(grade):
#     return grade >= 60
#
# is_grade = [67, 25, 35, 45, 77, 89, 63, 48, 32, 98]
#
# passing_grade = list(filter(grades, is_grade))
# print(passing_grade)


list1 = [
        ("Orange", 10),
        ("Apple", 9),
        ("Banana", 8)
         ]

x = list(filter(lambda lists: lists[1] >= 10, list1))
print(x)
