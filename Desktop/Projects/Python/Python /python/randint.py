import random

names = input("Enter everybody's name separated by coma: ")
name_list = names.split(',')
#choices = random.randint(1, len(name_list) -1)
#person_selected = random.choice(name_list)
print(f'{random.choice(name_list)} will pay the bill')
