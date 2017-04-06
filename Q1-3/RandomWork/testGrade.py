import sys

print('The arguments passed were: ')
print(sys.argv)

TestGrade = float(sys.argv[1])

if 97 <= float(TestGrade) <= 100:
    print('Your test grade is A+')
elif 93 <= float(TestGrade) <= 96:
    print('Your test grade is A')
elif 90 <= float(TestGrade) <= 92:
    print('Your test grade is A-')

elif 87 <= float(TestGrade) <= 89:
    print('Your test grade is B+')
elif 83 <= float(TestGrade) <= 86:
    print('Your test grade is B')
elif 80 <= float(TestGrade) <= 82:
    print('Your test grade is B-')

elif 77 <= float(TestGrade) <= 79:
    print('Your test grade is C+')
elif 73 <= float(TestGrade) <= 76:
    print('Your test grade is C')
elif 70 <= float(TestGrade) <= 72:
    print('Your test grade is C-')

elif 67 <= float(TestGrade) <= 69:
    print('Your test grade is D+')
elif 63 <= float(TestGrade) <= 66:
    print('Your test grade is D')
elif 60 <= float(TestGrade) <= 62:
    print('Your test grade is D-')

elif 0 <= float(TestGrade) <=59:
    print('You failed. F.')
else:
    print('Not a valid test grade.')


