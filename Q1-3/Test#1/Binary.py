dec = 0
bin = [2]

while sum(bin) > bin.count(1):
    bin1 = input("Please enter only 1's and 0's (10111): ")
    bin = [int(i) for i in str(bin1)]

for c in range(len(bin)):
    dec += bin[(c+1)*(-1)]*(2**c)
    print(dec)

print("The decimal number is: " + str(dec))


