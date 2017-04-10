#Create a GUI that shows the letter corresponding to the
# grade entered by the user using a QLineEdit. Use PAS scale.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class Example(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setGeometry(300, 300, 300, 250)
      self.resize(700, 300)
      self.move(50, 50)
      self.setStyleSheet("background-color:white;")
      self.setWindowTitle('Grade Convertor')

      self.text1 = QLineEdit(self)
      self.text1.resize(200, 40)
      self.text1.move(50, 80)
      self.text1.setPlaceholderText("Enter Grade 1-100")


      self.show()

  def grades(self):
      grade = {'A+': [97, 100], 'A': [93, 96], 'A-': [90, 92],
               'B+': [87, 89], 'B': [83, 86], 'B-': [80, 82],
               'C+': [77, 79], 'C': [73, 76], 'C-': [70, 72],
               'D+': [67, 69], 'D': [63, 66], 'D-': [60, 62],
               'F': [0, 59]}

        #use range for dic

def convertCal(self):
      if self.text1.toPlainText() is not "":
          cookie = int(self.text1.toPlainText())
          self.num.setValue(cookie * 488)

# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


#layout: QVBoxLayout
# so no need to set position

