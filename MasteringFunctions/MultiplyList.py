#Write a Python function to multiply all the numbers in a list. It should skip non-numeric values.
list = [1,2,3]
print(list)

def product():
    p = 1
    for i in range(len(list)):
        p *= list[i]
        print(p)

product()


