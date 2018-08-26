class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Smith', 70000)
print(bob.lastName())
print(sue.lastName())
bob.giveRaise(.10)
print(bob.pay)
