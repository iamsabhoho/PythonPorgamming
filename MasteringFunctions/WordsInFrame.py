#Write a function that takes a list of strings and prints them, one per line, in a rectangular frame.

list = ['This', 'is', 'a', 'test']

def Stars():
    star = len(max(list, key=len))
    print(star*'**')
    return star

    return i
def Words():
    for j in range(len(list)):
        print('*' + list[j] + '*')
    return j

Stars()
Words()
Stars()
