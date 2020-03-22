import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


date = datetime.time(2016, 7, 10)

Employee.set_raise_amt(1.05)

emp = 'Jhon-Doe-7000'
new_Emp = Employee.from_str(emp)
print(new_Emp)

print(Employee.is_workday(date))
