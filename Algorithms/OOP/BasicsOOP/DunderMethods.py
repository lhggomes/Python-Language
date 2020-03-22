"""
Dunder or Magic Methods are especific procedures that can run on your code.
For definition, we use the __ behind and after the name of the function, like the examples in sequence

"""

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
