import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
#convert str into list
s = temps.split()
#convert string list into integer list
si = list(map(int, s))
print(si, file=sys.stderr)
#find the min value
ms = [abs(i) for i in si]
m = min(ms)
print(m, file=sys.stderr)

ind = ms.index(m)

print(ind, file=sys.stderr)

print(s[ind])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
