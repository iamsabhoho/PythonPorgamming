# Don't let the machines win. You are humanity's last hope... found some commands online

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axislines = [input() for i in range(height)]

lines = [input() for i in range(height)]
n = [[j,i] for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "0"]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in n:
    pR, pD = ('-1 -1', '-1 -1')
    for x in range(height,0,-1):
        if [i[0],i[1]+x] in [j for j in n]: pD = ('%s %s' % (i[0], i[1]+x))
    for x in range(width,0,-1):
        if [i[0]+x,i[1]] in [j for j in n]: pR = ('%s %s' % (i[0]+x, i[1]))
    # Three coordinates: a node, its right neighbor, its bottom neighbor
    print('%s %s %s %s' % (i[0], i[1], pR, pD))
