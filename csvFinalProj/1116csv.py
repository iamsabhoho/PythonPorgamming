import csv
import datetime

gcCount = 0

#dictionary of student id
stdid = {} #read student id from the powerschool file
student_name = []
act1 = []

powerschool = {'Teacher Name:':'', 'Section:':'Python', 'Assignment Name:':'', 'Due Date:':'', 'Points Possible:':'10',
          'Extra Points:':'0', 'Score Type:':'Points','Student ID':'', 'Student Name':'', 'Points':''}

#name and read the files
fgoo = 'Test- GoogleClassroom.csv'
fps1 = 'PowerSchoolTemplateRobotics_pst.csv'

print('1-Read google Classroom file')

#open the file: input file
gcFile = open(fgoo)
gcData = csv.reader(gcFile)
gcDatadata = [row for row in gcData]
included_cols_name = [0, 1]

#find the number of activities in google classroom
activity = []
for i, row in enumerate(gcData):
    print('{}- '.format(i+1), end='')
    activity.append(row)
    print(row)

print('Activity Name: ' + str(len(gcDatadata[0])-3))

for i, col in enumerate(gcDatadata[0]):
    if i > 2:
        print('Activity-{} : {}'.format(i-2, col))

print("")

#due dates
dateL = []
week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
#month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "June": 6, "July": 7, "Aug": 8, "Sept": 9, "Oct": 10,
 #        "Nov": 11, "Dec": 12}
month = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"June", 7:"July", 8:"Aug", 9:"Sept", 10:"Oct",
         11:"Nov", 12:"Dec"}

dateStr = ''
for num, date in enumerate(gcDatadata[1]):
    if num > 2:
        for m in range(len(month)):
            if date[3:6] == month[m]:
                months = m+1
        day = week[datetime.datetime(int('20' + date[-2:]), months, int(date[:2])).weekday()]
        dateStr += day + ' ' + date[3:6] + ' ' + date[:2] + ' ' + '00:00:00 CST' + ' 20' + date[-2:]
        dateL.append(dateStr)
        dateStr = ''
powerschool['Due Date:'] = dateL

#student name
cnt = 0
for row in gcData:
    student_name.append(list(row[i] for i in included_cols_name))
    cnt = cnt + 1

for i in student_name:
    print(i)

gcData = csv.reader(gcFile)
included_cols_act1 = [2]
for row in gcData:
    act1.append(list(row[i] for i in included_cols_act1))

#close file
gcFile.close()

#start writing on output files
#open output files
psFile = open(fps1)
psData = csv.reader(psFile)
psDatadata = [row for row in psData]

powerschool['Teacher Name:'] = psDatadata[0][1]
powerschool['Section:'] = psDatadata[1][1]

#student id
sid = []
for i, row in enumerate(psDatadata):
    if i > 8:
        for j, n in enumerate(psDatadata[i]):
            if n == 0:
                sid.append(j)
powerschool['Student ID'] = sid

#close pws file
psFile.close()

def newname(n):
    #new files naming
    newname = 'Assignment'
    newname += str(num) + '.csv'
    return newname

#writing all the informations
for i in range(num):
    newfilepws = open(newname(i+1))
    writer = csv.writer(newfilepws, delimiter=',')
    writer.writerow(['Teacher Name:'] + [powerschool['Teacher Name:']])
    writer.writerow(['Section:']+[powerschool['Section:']])
    for n, a in enumerate(powerschool['Assignment Name:']):
        if n == i:
            writer.writerow(['Assignment Name:']+[a])
    for n, d in enumerate(powerschool['Due Date:']):
        if n == i:
            writer.writerow(['Due Date:']+[d])
    writer.writerow(['Points Possible'] + [powerschool['Points Possible:']])
    writer.writerow(['Extra Points:'] + [powerschool['Extra Points:']])
    writer.writerow(['Score Type:'] + [powerschool['Score Type:']])
    writer.writerow('')
    writer.writerow(['Student ID']+ ['Student Name']+ ['Points'])
    for n in range(len(powerschool['Student ID'])):
        writer.writerow([powerschool['Student ID'][n]]+ [powerschool['Student Name'][n]]+
                        [powerschool['Points'][(len(gcDatadata[0])-3*n)+i]])
    newfilepws.close()
