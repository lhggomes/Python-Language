from Algorithms.OOP.Factory.Person import Person


class Employer(Person):
    def __init__(self, sal, matr):
        super(Employer, self)
        salary = sal
        registration = matr
