#Python OOP

class Employee:

    #class variables:
    numOfEmp = 0
    raise_amount = 1.04
    numOfEng = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numOfEmp += 1

    def fullname(self):

        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp.fullname())

class Engineer(Employee):

    def __init__(self, first, last, pay, department):
        super().__init__(first, last, pay)
        self.department = department

        Employee.numOfEng += 1

    @classmethod
    def howManyEng(cls):
        print('The number of engineers: ', cls.numOfEng)


dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'User', 60000, 'Java')


eng1 = Engineer('Testing', 'Name', 10000, 'Science')
eng2 = Engineer('Jane', 'Smith', 70000, 'Math')

print(eng1.department)
print(Engineer.numOfEng)

eng2.howManyEng()

#print(isinstance(dev1, Developer))
