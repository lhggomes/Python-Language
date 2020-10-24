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
        self.email = firstName + '.' + lastName + "@gmail.com"

        self.num_emplo += 1

    #This Method change the __add__ function
    def __add__(self, other):
        return self.pay + other.pay


ep1 = Employee('Lucas', 'Gomes', 5466)
ep2 = Employee('Atillyo', 'Ramos', 4557)

# Using DunderMethods
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))
#Using the function who has changed
print(ep1 + ep2)

