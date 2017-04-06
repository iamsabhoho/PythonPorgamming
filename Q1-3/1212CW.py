#validating an email address
import re
#it has to contain a '@'

def EmailValid():
    testing ='testing@csi.org'
    check = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', testing)

    if check == None:
        print('Syntax')
        raise ValueError('Syntax')

