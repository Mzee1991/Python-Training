#!/usr/bin/python3

class Employee:

    raise_amount = 1.04
    num_of_emps = 0 # No. of employees

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def details(self):
        print("Name: {} {}".format(self.first, self.last))
        print("Salary: {}".format(self.pay))
        print("Email: {}\n".format(self.email))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp_1 = Employee('Mzee', 'John', 20000)
emp_2 = Employee('Joe', 'lop', 30000)
print(Employee.num_of_emps)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
