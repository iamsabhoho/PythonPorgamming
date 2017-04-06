#This serve the purpose of library to save teh functions will be used in store.py

employee  = {'first_name': None, 'last_name': None, 'age': None,
             'since': None, 'role': None, 'daysWorked': None, 'salary': None}

newE = []

#first_name, last_name, age, since, role, daysWorked, salary
def register(first_name, last_name, age, since, daysWorked, role, salary):
    """
    This function registers for new employee
    :param first_name: string
    :param last_name: string
    :param age: int
    :param since: string
    :param role: string
    :param daysWorked: int
    :param salary: int
    :return:
    """

    temp = employee.copy()
    temp['first_name'] = first_name
    temp['last_name'] = last_name
    temp['age'] = age
    temp['since'] = since
    temp['daysWorked'] = daysWorked
    temp['role'] = role
    temp['salary'] = salary

    newE.append(temp)

def showingE():
    for num, e in enumerate(newE):
        if e['daysWorked'] != 1:
            print('Staff #%r: %s %s age %r has been working %r days since %s as a %s for USD %r'
                  % (num+1, e['first_name'], e['last_name'], e['age'], e['daysWorked'], e['since'], e['role'], e['salary']))
        else:
            print('Staff #%r: %s %s age %r has been working %r day since %s as a %s for USD %r'
                  % (num+1, e['first_name'], e['last_name'], e['age'], e['daysWorked'], e['since'], e['role'], e['salary']))

def addingDays():
    for e in newE:
        e['daysWorked'] += 1


def removeE():




