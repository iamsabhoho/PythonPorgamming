#This program finds those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included).

print('These are divisible by 7: ')
print(' ')
for i in range(1500, 2701):
    if i%7 == 0:
        print(i)
        continue

print(' ')
print('These are the multiple of 5: ')
print(' ')
for j in range(1500, 2701):
    if j%5 == 0:
        print(j)
        continue
