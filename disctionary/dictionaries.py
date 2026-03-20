student = {"name": "Kali", "age": 25, "city": "New York"}

print(student, type(student)) # Output: Kali <class 'dict'> 

print(student["name"]) # Output: Kali
print(student["age"]) # Output: 25
print(student["city"]) # Output: New York   


student["age"] = 26 # updates the value of age to 26
print(student) # Output: {'name': 'Kali', 'age': 26, 'city': 'New York'}   

print(student.keys()) # Output: dict_keys(['name', 'age', 'city'])
print(student.values()) # Output: dict_values(['Kali', 26, 'New York'])
print(student.items()) # Output: dict_items([('name', 'Kali'), ('age', 26), ('city', 'New York')])

print(len(student)) # Output: 3
print(max(student)) # Output: name (since 'name' is the largest key in alphabetical order)
print(min(student)) # Output: age (since 'age' is the smallest key in alphabetical order)

student.pop("city") # removes the key 'city' and its value from the dictionary
print(student) # Output: {'name': 'Kali', 'age': 26}

student.clear() # removes all items from the dictionary
print(student) # Output: {} 




