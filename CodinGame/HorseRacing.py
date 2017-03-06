import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
piHorse = []



for i in range(n):
    pi = int(input())
    piHorse.append(n)

piHorse.sort()

for j in range(len(piHorse) - 1):
    diff = abs(piHorse[j] - piHorse[j+1])
    if diff < result:
        result = diff

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer: " + result)
