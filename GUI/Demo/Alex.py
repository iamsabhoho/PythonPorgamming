#QCheckBox
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon

class CheckDemo(QWidget):
    def __init__(self):
        super(CheckDemo, self).__init__()
        self.init()

    def init(self):
        self.setGeometry(400, 400, 450, 350)
        self.setWindowTitle('CheckBox Demo')


        # --- add a checkbox
        self.check = QCheckBox('This is a checkbox', self)
        self.check.setTristate(True)
        self.check.resize(250, 30)
        self.check.stateChanged.connect(self.dosth)
        self.check.move(150, 30)
        self.check.setIcon(QIcon("icon.png"))


        # --- add a button
        self.btn1 = QPushButton('Reset', self)
        self.btn1.setToolTip('This button reset the ckeckbox')
        self.btn1.resize(250, 90)
        self.btn1.move(100, 100)
        self.btn1.clicked.connect(self.reset)

        # --- add another button for disabling and enabling the checkbox
        self.btn2 = QPushButton('Disable/Enable', self)
        self.btn2.setToolTip('This button disable/enable the ckeckbox')
        self.btn2.resize(250, 90)
        self.btn2.move(100, 200)
        self.btn2.clicked.connect(self.toggle)



        self.show()

    # --- check whether the box is checked
    def dosth(self):
        '''
        if self.check.isChecked():
            self.setWindowTitle('The checkbox was checked')
        else:
            self.setWindowTitle('The checkbox was unchecked')
        '''

        state = self.check.checkState()

        if state == 0:
            self.setWindowTitle('The checkbox was unchecked')
        elif state == 2:
            self.setWindowTitle('The checkbox was checked')
        else:
            self.setWindowTitle('The checkbox was unchanged')

    def reset(self):
        self.check.setChecked(False)
        self.setWindowTitle('CheckBox Demo')

    def toggle(self):

        # --- the first one is better
        '''
        if self.check.isEnabled():
            self.check.setEnabled(False)
            self.setWindowTitle('It is disabled')
        else:
            self.check.setEnabled(True)
            self.setWindowTitle('It is enable')
        '''

        if self.check.isCheckable():
            self.check.setCheckable(False)
            self.setWindowTitle('It is disabled')
        else:
            self.check.setCheckable(True)
            self.setWindowTitle('It is enable')




# --- main program
app = QApplication(sys.argv)
w = CheckDemo()
sys.exit(app.exec_())



