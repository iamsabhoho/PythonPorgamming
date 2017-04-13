import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
   def __init__(self):
      super(Example, self).__init__()

      self.initUI()

   def initUI(self):

      cal = QCalendarWidget(self)
      cal.setGridVisible(True)
      cal.move(20, 20)
      cal.clicked[QDate].connect(self.showDate)

      #lbl = label widgets

      self.lbl = QLabel(self)
      date = cal.selectedDate()
      self.lbl.setText(date.toString())
      self.lbl.move(20, 200)

      self.setGeometry(100, 100, 400, 300)
      self.setWindowTitle('Calendar')

      self.show()

   def showDate(self, date):
      self.lbl.setText(date.toString())


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
