#this program will help you find out if you should major in computer science

import sys

print("Should you major in computer science?")
print("You will find out soon :)")
print(" ")
print(" ")

if input("Do you like computer science? (y/n) ") == "y":
    if input("Have you learned programming before? (y/n) ") == "y":
        sys.exit("Yes, you should major it and keep learning it")
    else:
        print("Start learning programming is not too late")
else:
    if input("Do you want to major in computer science? (y/n) ") == "y":
        sys.exit("Start learning programming is not too late")
    else:
        sys.exit("Maybe you have other interest, that is fine too ;) But computer science is fun")
