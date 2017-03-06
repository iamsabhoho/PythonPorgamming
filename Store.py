#This is the main program that calls out functions from StaffLib.py
import StaffLib as sl
#'John', 'Sena', 30, '11-Nov-2016', 'driver', 0, 1000

sl.register(first_name='John', last_name='Sena', age=30, since='11-Nov-2016',
                  daysWorked= 0, role='driver', salary = 1000)
sl.register(first_name='Leo', last_name='Messi', age=29, since='24-Jun-1987',
                  daysWorked= 12, role='soccerCaptain', salary = 5000000)
sl.register(first_name='Neymar', last_name='Jr', age=24, since='05-Feb-1992',
                  daysWorked= 25, role='soccerPlayer', salary = 4000000)
sl.register(first_name='Lady', last_name='Gaga', age=30, since='28-Mar-1986',
                  daysWorked= 50, role='singer', salary = 9000000)
sl.register(first_name='Cara', last_name='Delevingne', age=24, since='12-Aug-1992',
                  daysWorked= 100, role='model', salary = 7000000)

sl.showingE()
sl.addingDays()
sl.showingE()
