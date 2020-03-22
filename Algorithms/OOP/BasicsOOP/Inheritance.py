class Employee:
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.first = firstName
        self.last = lastName
        self.pay = pay
        self.email = firstName + '.' + lastName + "@aperam.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, firstName, lastName, pay, prog_lang):
        super().__init__(firstName, lastName, pay)
        self.pro_lang = prog_lang

    pass


class Manager(Employee):
    def __init__(self, firstName, lastName, pay, employees: None):
        super().__init__(firstName, lastName, pay)
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
            print('-->', emp.fullname())

dev_1 = Developer('Lucas', 'Gomes', 9000, 'Python')
print(dev_1.email)
print(dev_1.pro_lang)
