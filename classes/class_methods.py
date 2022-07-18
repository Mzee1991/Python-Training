#!/usr/bin/python3

class Employee:

    raise_amt = 1.04
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
       self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee('Mzee', 'Jonh', 40000)
emp_2 = Employee('Domino', 'Rex', 35000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
