#Write a multiplication table range 1-10

num = int(input('Please enter a number of a multiplication table(1-10): '))

for i in range(1,11):
    x = num*i
    print(str(num) + ' x ' + str(i) + ' = ' + str(x))
