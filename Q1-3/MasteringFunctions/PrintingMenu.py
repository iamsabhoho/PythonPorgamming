#Write a function for printing menus in the terminal.
#The input is a list of options, and the output is the option selected by the user.

print('The options are: ')
#list = input()
#menu = ['Meat','Chicken','Fish']
menu = []
print(menu)
print()

def options(menu):
    menu = input('Please enter the options: ')
    for i in range(len(menu)):
        option = i + 1
        print(str(option) + menu[i])

    user = input('What is your preference? Press X to exit: ')
    if user == 'x':
        exit()
    elif user == '1':
        print(menu[0])
        return user
    elif user == '2':
        print(menu[1])
        return user
    else:
        print(menu[2])
        return user
    return user

options()
