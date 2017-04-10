#Create a GUI with two buttons A, and B.
# When a button is pressed, the title of the GUI changes to the name of the button pressed.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox

class Example(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setGeometry(300, 300, 300, 250)
      self.resize(700, 300)
      self.move(50, 50)
      self.setStyleSheet("background-color:white;")
      #self.setWindowTitle('Clicking Button')

      # add a push button
      self.btn1 = QPushButton('Button A', self)
      self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
      self.btn1.resize(250, 200)
      self.btn1.move(50, 50)
      self.btn1.clicked.connect(self.buttonA)


      self.btn2 = QPushButton('Button B', self)
      self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
      self.btn2.resize(250, 200)
      self.btn2.move(400, 50)
      self.btn2.clicked.connect(self.buttonB)

      self.show()

  def buttonA(self):
      self.setWindowTitle('Botton A Clicked')

  def buttonB(self):
      self.setWindowTitle('Botton B Clicked')


# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
