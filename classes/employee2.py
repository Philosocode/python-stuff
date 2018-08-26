# Python Object-Oriented Programming
# Instance Variables are unique to each instance
# Class Variables are the same across all instances


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


# Pass in the values specified in the __init__ method
print(Employee.num_of_emps, "employees.")
emp_1 = Employee('Corey', 'Schafer', 50000)  # unique instance
print(Employee.num_of_emps, "employees.")
emp_2 = Employee('Test', 'User', 60000)  # unique instance
print(Employee.num_of_emps, "employees.")

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(emp_1.pay, "before raise.")
# Employee.raise_amount = 2
emp_1.raise_amount = 1.05
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay, "after raise.")
print(emp_2.pay, "after raise.")
print(emp_1.raise_amount)
print(emp_2.raise_amount)
