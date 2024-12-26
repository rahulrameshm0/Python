# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self, subject_name):
#         print(f"Helo, I am {self.name} and I teach {subject_name}")
# person_1 = Person("Jenny",25)
# print(person_1.name)
# print(person_1.age)
# person_1.display("Python")
#
# # person_2 = Person()
# # person_2.name = "laura"
# # person_2.age = "25"
# # print(person_2.name)
# #
# # person_2 = Person()
# # person_2.name = "Charlie"
# # person_2.age = "35"
# # print(person_2.name)
# #
# # person_2 = Person()
# # person_2.name = "Anny"
# # person_2.age = "28"
# # print(person_2.name)


# def check_scope():
#     def do_local():
#         test = "do local test"
#     def do_non_local():
#         nonlocal test
#         test = "do non local test"
#     def do_global():
#         global test
#         test = "global test"
#     test = "Global"
#     print(f"Testing scope: {test}")
#     do_non_local()
#     print(f"Testing Global: {test}")
#     do_global()
#     print(f"Check value after do global: {test}")
# check_scope()
# print(f"Check value after do global: {test}

class Myclass:
    def hello(self,name):
        print(f"Hello {name}, how is your day?")

x = Myclass()
name = "Rahul Ramesh"
x.hello(name)
