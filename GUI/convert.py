import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox

class Example(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setGeometry(300, 300, 300, 250)
      self.setStyleSheet("background-color:black;")
      self.setWindowTitle('Second GUI')
      self.setWindowIcon(QIcon("icon.png"))
      self.show()

  def initUI(self):
      self.btn1 = QPushButton('Convert to USD', self)
      self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
      self.btn1.resize(200, 20)
      self.btn1.move(50, 50)
      self.btn1.clicked.connect(self.convert)

      self.text1 = QTextEdit(self)
      self.text1.resize(200, 40)
      self.text1.move(50, 80)
      self.text1.setPlaceholderText("Enter TWD")
      self.num = QDoubleSpinBox(self)
      self.num.setMaximum(200000)
      self.num.setMinimum(0)
      self.num.setSuffix(" USD")
      self.num.resize(200,30)
      self.num.move(50,130)
      self.show()

  def convert(self):
   if self.text1.toPlainText() is not "":
       twd = int(self.text1.toPlainText())
       self.num.setValue(twd / 30.12)

# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
