#Make a script that determines if a string passed as an argument in the terminal is a palindrome.
from string import whitespace
w = input('Please enter a word: ')
print(w)
nw = w.replace(' ','')
print(nw)

flag = 0

for i in range(int(len(nw)/2)):
    if nw[i] == nw[(i+1)*(-1)]:
        continue
    else:
        flag = 1
        break

if flag == 1:
    print('This is not a palindrome.')
else:
    print('This is a palindrome.')
