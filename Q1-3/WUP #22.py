password = input('Please enter a new password (min len is 8 characters'
                 'and it can only contain letters and at least one numbers):')

if len(password) >= 8:
    if password.isalnum():

    elif password.isalpha():
    elif password.isdecimal():
    else:
        print('This is not a valid password.')
else:
    print('This password is too short.')



def printPicnic(items, lwidth, rwidth):
    """
    adjust the place of the numbers
    :param items:
    :param lwidth:
    :param rwidth:
    :return:
    """
    print('PICNIC ITEMS'.center(lwidth + rwidth, '-'))
    for k, v in items.items():
        print(k.ljust(lwidth, '.') + str(v).rjust(rwidth))


picnic = {'sandwiches' : 4, 'apples': 12, 'cups':4, 'cookies':8000}
printPicnic(picnic, 12, 5)
printPicnic(picnic, 20, 6)
