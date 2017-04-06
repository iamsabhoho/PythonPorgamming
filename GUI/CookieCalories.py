import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox

class Example(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setGeometry(300, 300, 300, 250)
      self.resize(600, 300)
      self.move(50, 50)
      self.setStyleSheet("background-color:white;")
      self.setWindowTitle('CookieConvert GUI')

      self.btn1 = QPushButton('Convert to Calories', self)
      self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
      self.btn1.resize(200, 20)
      self.btn1.move(50, 50)
      self.btn1.clicked.connect(self.convertCal)

      self.text1 = QTextEdit(self)
      self.text1.resize(200, 40)
      self.text1.move(50, 80)
      self.text1.setPlaceholderText("Enter Number of Cookies")
      self.num = QDoubleSpinBox(self)
      self.num.setMaximum(200000)
      self.num.setMinimum(0)
      self.num.setSuffix(" Cal")
      self.num.resize(200,30)
      self.num.move(50,130)



      self.btn2 = QPushButton('Convert to Cookies', self)
      self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
      self.btn2.resize(200, 20)
      self.btn2.move(350, 50)
      self.btn2.clicked.connect(self.convertCookie)

      self.text2 = QTextEdit(self)
      self.text2.resize(200, 40)
      self.text2.move(350, 80)
      self.text2.setPlaceholderText("Enter Number of Calories")
      self.num2 = QDoubleSpinBox(self)
      self.num2.setMaximum(200000)
      self.num2.setMinimum(0)
      self.num2.setSuffix(" Cookies")
      self.num2.resize(200,30)
      self.num2.move(350,130)
      self.show()

  def convertCal(self):
      if self.text1.toPlainText() is not "":
          cookie = int(self.text1.toPlainText())
          self.num.setValue(cookie * 488)

  def convertCookie(self):
      if self.text2.toPlainText() is not "":
          cal = int(self.text2.toPlainText())
          self.num2.setValue(cal / 488)



# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
