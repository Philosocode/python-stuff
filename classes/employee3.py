# Python Object-Oriented Programming
# Regular Methods, Class Methods, Static Methods
import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # the instance = self
        self.first = first
        self.last = last
        self.pay = pay
        # Notice: not "self.first", but just "first"
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternative Constructor: string with hyphens
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5:
            return False
        elif day.weekday() == 6:
            return False
        return True


# Pass in the values specified in the __init__ method
emp_1 = Employee('Corey', 'Schafer', 50000)  # unique instance
emp_2 = Employee('Test', 'User', 60000)  # unique instance

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

# emp_str_1 = "John-Doe-70000"
# new_emp_1 = Employee.from_string(emp_str_1)
# emp_str_2 = "Steve-Smith-20000"
# new_emp_2 = Employee.from_string(emp_str_2)
# emp_str_3 = "Jane-Doe-90000"
# new_emp_3 = Employee.from_string(emp_str_3)

# print(new_emp_1.fullname())
# print(new_emp_2.fullname())
# print(new_emp_3.fullname())

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = employee(first, last, pay)
# print(new_emp_1.email, new_emp_1.pay)

# Employee.set_raise_amount(2.22)
# The same as Employee.raise_amount = 2.22
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
