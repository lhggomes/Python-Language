from Algorithms.OOP.Factory.Person import Person


class Employer(Person):
    def __init__(self, sal, matr, name, age, rg):
        Person.__init__(name, age, rg)
        salary = sal
        registration = matr



