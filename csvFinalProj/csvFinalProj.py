import csv

gcCount = 0

#dictionary of student id
stdid = {'Chang, Stephanie' : 20140800050, 'Chen, Cici' : 20120700011,
           'Chiang, Darren': 20070200002, 'Ho, Sabrina': 20141000057,
           'Huang, Daniel': 20140900054, 'Tai, Alex': 20120800023}

powerschool = {'Teacher Name:':'', 'Section:':'Python', 'Assignment Name:':'', 'Due Date:':'', 'Points Possible:':'10',
          'Extra Points:':'0', 'Score Type:':'Points','Student ID':'', 'Student Name':'', 'Points':''}

#get the student id by using their names
def getid(name):
    return stdid[name]

fgoo = 'GoogleActivities.csv'
fps = 'PowerSchoolTemplate.csv'

print('1-Read google Classroom file')

#open the file
gcFile = open(fgoo)
gcData = csv.reader(gcFile)

#show all the rows in the file
activity = []
for i, row in enumerate(gcData):
    print('{}- '.format(i+1), end='')
    activity.append(row)
    print(row)

print('Number of activities found: ' + str(len(activity[0])-3))

for i, col in enumerate(activity[0]):
    if i > 2:
        print('Activity-{} : {}'.format(i-2, col))

print("")

#students names
print("Student's name")
names = []
for i, row in enumerate(activity):
    if i > 2:
        print('Student - {} : {}, {}'.format(i-2, row[1],row[0]))
        names.append(row[1] + ', ' + row[0])
gcCount = len(names)

print("")

#students ids
print("Student's ID")
sid = []
for i in range(int(gcCount)):
    sid.append(getid(names[i]))
    print('Student ID - {} : {}'.format(i+1, sid[i]))

print("")

#students points
print("Student's points")
points = []
for i, row in enumerate(activity):
    if i > 2:
        print("Student's points - {} : {}, {}, {}, {}".format(i-2, row[3],row[4], row[5], row[6]))
        points.append(row[3] + ', ' + row[4] + ', ' + row[5] + ', ' + row[6])

print("")

#open the file
with open(fps, 'w+') as csvfile:
    fieldnames = ['sid', 'name', 'points']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#append activity[], name[] in fps
    writer.writeheader()
    for i in range(gcCount):
        writer.writerow({'sid': sid[i], 'name': names[i], 'points' : points[i]})
csvfile.close()
