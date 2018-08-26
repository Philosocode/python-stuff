# Python Object-Oriented Programming
# Subclasses


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):  # the instance = self
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    # Doesn't affect Employee.raise_amount
    raise_amount = 5

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    # employees = a List of employees supervised
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp)


dev_1 = Developer("Tam", "Le", 100000, "Python")
dev_2 = Developer("John", "Cena", 1, "Jumbo")
manager_1 = Manager("Darron", "Ta", 900000, [dev_1, dev_2])

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)
# print(manager_1.email)
manager_1.add_emp("JoeJoe")
manager_1.remove_emp(dev_1)
manager_1.remove_emp(dev_2)
print(manager_1.print_emps())

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
