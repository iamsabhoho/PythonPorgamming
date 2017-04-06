#This program calculate the defualt number average

def list_average(x = [1,2,3,3,4]):
    a = 0
    for i in x:
        a += i
        result = a/len(x)
    return result

print(list_average())
