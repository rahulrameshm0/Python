dict1 = {"Rahul": {"Age": 25, 'Department': "CS",},
        "Afam": {"Age": 25, "Department": "CS"},
        "Sonny": {"Age": 21, "Department": "CS"}
         }

dict2 = {key: value for (key, value) in dict1.items() if value["Age"] == 25}
for index, (name, details) in enumerate(dict2.items(), start=1):
    print(f" Name: {name}, Age: {details["Age"]:}, Department: {details["Department"]}")