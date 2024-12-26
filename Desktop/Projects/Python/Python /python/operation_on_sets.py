set_1 = {1,5,4,3,5,8}
set_2 = {2,4,6,9,10,12}

print(set_1 | set_2)

set_1 = {'Rahul','Rohit','Afam','Fazil','Asif'}
set_2 = {'Rahul','Afam','Fazil','Asif','Ramesh'}
print(set_1.union(set_2))

set_1 = {'Rahul','Rohit','Afam','Fazil','Asif'}
set_2 = {'Rahul','Afam','Fazil','Asif','Ramesh,ramesh'}
print(set_1.intersection(set_2))
set_1 = {'Rahul','Rohit','Afam','Fazil','Asif','rahul'}
set_2 = {'Rahul','Afam','Fazil','Asif','Ramesh'}
set_1.update(['ramesh'])
print(set_1)

set_1 = {3,4,8,9,12,16}
set_2 = {2,3,8,10,15,16}
print(set_1 & set_2)

set_1 = {5,6,9,15,19,25}
set_2 = {9,16,24,15,8,4}
print(set_1 | set_2)

set_1 = {5,6,9,15,19,25}
set_2 = {9,16,24,15,8,4}
print(set_1 - set_2)

set_1 = {'Rahul','Binsy','Rohit'}
set_2 = {'Afam','Fazil','Binsy'}
set_3 = {'Ashiq','Rahul','Ramesh'}
print(set_1.difference(set_2,set_3))


set_1 = {'Rahul','Binsy','Fazil'}
set_2 = {'Afam','Fazil','Binsy'}
set_3 = {'Ashiq','Rahul','Ramesh'}
print(set_1 ^ set_2 ^ set_3)

set_1 = {'Rahul','Binsy','Fazil'}
set_2 = {'Afam','Rohit','Ramesh'}
print(set_1.isdisjoint(['kiran','Fazil']))

set_1 = {'Rahul','Binsy','Fazil'}
set_2 = {'Afam','Rohit','Ramesh'}
print(set_1.issubset(['kiran','Fazil']))

set_1 = {'Rahul','Binsy','Fazil'}
set_2 = {'Afam','Rohit','Ramesh'}
print(set_1.issuperset(['Rahul', 'Binsy', 'Fazil']))