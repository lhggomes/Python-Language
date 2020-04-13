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
dev_2 = Developer('Matheys', 'Dutra', 9000, 'PHP')
print(dev_1.email)
print(dev_1.pro_lang)

mgr_1 = Manager('Fernando', 'Smith', 1983, [dev_1])
print(mgr_1.email)



mgr_1.add_emp(dev_2)

mgr_1.print_emps()

print(dev_1.__dict__());

print(isinstance(mgr_1, Developer))

print(dev_1.__slots__());