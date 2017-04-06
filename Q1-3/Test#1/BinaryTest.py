dec = 0
bin = [2]

while sum(bin) > bin.count(1):
    bin1 = str(input("Please enter only 1's and 0's (10111): "))
    for i in bin1:
        bin[i] = int(i)

for c in range(len(bin)):
    dec += bin[(c+1)*(-1)]*(2**c)

print("The decimal number is: " + str(dec))


