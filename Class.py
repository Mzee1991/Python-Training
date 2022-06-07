#!/usr/bin/python3

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def details(self):
        print("Name: {} {}".format(self.first, self.last))
        print("Salary: {}".format(self.pay))
        print("Email: {}\n".format(self.email))


emp_1 = Employee('Mzee', 'John', 20000)
emp_2 = Employee('Joe', 'lop', 30000)

# print(emp_1) these print the above Employee instances
# print(emp_2)
# Use the above created instances to access the attributes of the class

# print(emp_1.email)
# print(emp_2.email)
emp_1.details()
emp_2.details()
