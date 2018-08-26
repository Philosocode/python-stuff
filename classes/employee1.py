# Python Object-Oriented Programming
# Instance Variables


class Employee:
    def __init__(self, first, last, pay):  # the instance = self
        self.first = first
        self.last = last
        self.pay = pay
        # Notice: not "self.first", but just "first"
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Pass in the values specified in the __init__ method
emp_1 = Employee('Corey', 'Schafer', 50000)  # unique instance
emp_2 = Employee('Test', 'User', 60000)  # unique instance

print(emp_1.fullname())
print(Employee.fullname(emp_1))

print(emp_2.fullname())
print(Employee.fullname(emp_2))

# print(emp_1)
# print(emp_2)
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())
