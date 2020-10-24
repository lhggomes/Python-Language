class Employee:
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.first = firstName
        self.last = lastName
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@aperam.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.slipt(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None



emp1 = Employee('Lucas', 'Gomes', 4566)
emp1.fullname = 'Lucas Silva'
