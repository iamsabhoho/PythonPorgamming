import random

# here set the number of digits in the game
numDigits = 5

# create the secret number as a concatenation of string digits
secretNumber = ''
for i in range(numDigits):
   secretNumber += str(random.randint(0, 9))

# initialize the tries counter for the user
iterations = 1
# initialize the blackHit to zero. Needed to enter the while loop
blackHits = 0
while blackHits < numDigits:
    # Ask for user input and restart counter of white and black hits
    userNumber = input('Try to guess the secret number (enter {} digits)'.format(numDigits))
    blackHits = 0
    whiteHits = 0
    cntDigit = 0
    iterations += 1

    #start the loop to check every digit in the user input
    for d in userNumber:

    #ask if the digit exist in the secret number
        if d in secretNumber:
            # position of digit in the secret number
            posDigit = secretNumber.index(d)
            # check if positions match
            if cntDigit == posDigit:
                blackHits += 1
            else:
                whiteHits += 1
        # check next digit in the user guess
        cntDigit += 1
# show hits
print("You have {} white hits and {} black hits".format(whiteHits, blackHits))
# the user won the game, show the number of tries he/she took
print("Congratulations you win in {} tries".format(iterations))
