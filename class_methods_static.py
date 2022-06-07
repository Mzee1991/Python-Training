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

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Mzee', 'Jonh', 40000)
emp_2 = Employee('Domino', 'Rex', 35000)

import datetime
my_date = datetime.date(2022, 6, 10)

print(Employee.is_workday(my_date))
