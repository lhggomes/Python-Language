class Employee:
    raise_amount = 1.04
    num_emplo = 0

    def __init__(self, firstName, lastName, pay):
        self.first = firstName
        self.last = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + "@aperam.com"

        self.num_emplo += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Corey', 'Schafar', 5000)
emp2 = Employee('Lucas', 'Gomes', 4560)
