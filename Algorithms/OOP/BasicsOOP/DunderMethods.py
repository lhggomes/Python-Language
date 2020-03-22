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

#Using DunderMethods

print(int.__add__(1,2))
print(str.__add__('a', 'b'))