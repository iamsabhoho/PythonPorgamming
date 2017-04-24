#QDockWidget
import sys
from PyQt5.QtWidgets import QApplication, QDockWidget, QWidget, QPushButton

class dockDemo(QWidget):
    def __init__(self):
        QWidget.__init__(self)


    def init(self):
        self.setGeometry(300, 300, 300, 250)
        self.setStyleSheet('background-color: white;')

        self.btn1 = QPushButton('Button', self)

        self.dock1 = QDockWidget('My First Dock', self)
        self.dock1.move(20, 20)
        self.dock1.setWidget(self.btn1)
        self.dock1.setFloating(False)
        self.dock1.setFeatures(self.dock1.AllDockWidgetFeatures)

        self.show()

# --- main program
app = QApplication(sys.argv)
w = dockDemo()
w.init()
sys.exit(app.exec_())
