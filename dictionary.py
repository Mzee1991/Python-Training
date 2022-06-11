#!/usr/bin/python3

student = {'name': 'John', 'age': 25, 'Courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student['Courses'])

# In the above example the keys include--name, age, and Courses
# Keys can be an immutable data types, usually strings or integers, e.g

student = {1: 'John', 'age': 15}
print(student[1])

# Try accessing a key that doesn't exit and see what happens

print(student['phone'])

print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not_found'))

# How to add a new entry to our dictionary

student['phone'] = '0781-263379'

# How to update the different keys of the dictionary

student.update({'name': 'Jane', 'age': 24, 'phone': '0781-263379'})
print(student)

# To delete a specific key and it's value
# method 1 with del

del student['age']
print(student)

# method 2---pop methd

age = student.pop('age')
print(age)

# looping thru keys and values

# numbers of keys
print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)


