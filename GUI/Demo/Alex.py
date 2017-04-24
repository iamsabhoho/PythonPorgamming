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


class Ultimate(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(500, 300, 800, 450)
        self.setWindowTitle('NYU Housing Application')

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, "Personal Information")
        self.addTab(self.tab2, "Dorm Preferences")
        self.addTab(self.tab3, "Lifestyle Questionnaire")
        self.addTab(self.tab4, "Terms of Condition")
        self.addTab(self.tab5, "Confirmation Page")

        self.tab_1()
        self.tab_2()
        self.tab_3()
        self.tab_4()
        self.tab_5()

        self.show()

    def tab_1(self):
        layout = QFormLayout()
        self.tab1.setLayout(layout)

        # --- add all elements
        self.pb = QProgressBar(self)
        self.pb.setValue(0)
        self.txt1 = QLineEdit(self)
        self.txt1.setPlaceholderText("Alex")
        self.txt2 = QLineEdit(self)
        self.txt2.setPlaceholderText("Tai")
        self.txt3 = QLineEdit(self)
        self.cal1 = QCalendarWidget(self)
        self.cal1.setGridVisible(True)
        self.cal1.move(20, 50)
        self.dock1 = QDockWidget('Select your birthday', self)
        self.dock1.setWidget(self.cal1)
        self.dock1.move(105, 120)
        self.dock1.setFloating(False)
        self.dock1.setFeatures(self.dock1.DockWidgetClosable | self.dock1.DockWidgetMovable)
        self.dock1.setFeatures(self.dock1.NoDockWidgetFeatures)
        self.txt3.setPlaceholderText("Johnson Tai")
        self.txt4 = QLineEdit(self)
        self.txt4.setPlaceholderText("+886 975365270")
        self.btn = QPushButton('--->', self)
        self.btn.clicked.connect(self.nextTab)

        # --- display all elements
        layout.addRow(self.pb)
        layout.addRow('First Name', self.txt1)
        layout.addRow('Last Name', self.txt2)
        layout.addRow('Birthday', self.dock1)
        layout.addRow('Emergency Contact Full Name', self.txt3)
        layout.addRow('Emergency Contact Number', self.txt4)
        layout.addRow('Next Section', self.btn)

    def tab_2(self):
        layout = QFormLayout()
        self.tab2.setLayout(layout)

        # --- add all elements
        self.pb = QProgressBar(self)
        self.pb.setValue(25)
        self.lb = QLabel(self)
        self.lb.setToolTip('https://goo.gl/pB9kmb')
        self.lb.setText("<a href='https://goo.gl/P2WHiy'>Click Here</a>")
        self.lb.setOpenExternalLinks(True)
        self.cb = QComboBox(self)
        self.cb.addItem("Founders Hall")
        self.cb.addItem("Lipton Hall")
        self.cb.addItem("University Hall")
        self.cb.addItem("Palladium Hall")
        self.cb.addItem("Rubin Hall")
        self.cb.addItem("Brittany Hall")
        self.btn1 = QPushButton('--->', self)
        self.btn1.clicked.connect(self.nextTab)

        # --- display all elements
        layout.addRow(self.pb)
        layout.addRow('For more information on NYU Residential Halls: ', self.lb)
        layout.addRow('Preferred Dorm', self.cb)
        layout.addRow('Next Section', self.btn1)

    def tab_3(self):
        layout = QFormLayout()
        self.tab3.setLayout(layout)

        # --- add all elements
        self.pb = QProgressBar(self)
        self.pb.setValue(50)
        self.num1 = QSpinBox(self)
        self.num1.setMaximum(10)
        self.num1.setMinimum(1)
        self.num2 = QSpinBox(self)
        self.num2.setMaximum(24)
        self.num2.setMinimum(1)
        self.num3 = QSpinBox(self)
        self.num3.setMaximum(24)
        self.num3.setMinimum(1)
        self.btn2 = QPushButton('--->', self)
        self.btn2.clicked.connect(self.nextTab)

        # --- display all elements
        layout.addRow(self.pb)
        layout.addRow('On a scale of 10, how clean are you? (10: Very Clean)', self.num1)
        layout.addRow('When do you normally sleep? (24hr Clock)', self.num2)
        layout.addRow('When do you normally wake up? (24hr Clock)', self.num3)
        layout.addRow('Next Section', self.btn2)

    def tab_4(self):
        layout = QFormLayout()
        self.tab4.setLayout(layout)

        # --- add all elements
        self.pb = QProgressBar(self)
        self.pb.setValue(75)
        self.lb1 = QLabel(self)
        self.lb1.setText("Please read these Terms and Conditions carefully before using the Ultimate GUI.")
        self.lb2 = QLabel(self)
        self.lb2.setToolTip('Terms')
        self.lb2.setText("<a href='https://termsfeed.com/terms-conditions/c54a21aa69c7585a026e503ceeb87519'>Click Here to View</a>")
        self.lb2.setOpenExternalLinks(True)
        self.cb = QCheckBox('I agree to the terms and conditions', self)
        self.btn3 = QPushButton('Yes', self)
        self.btn3.clicked.connect(self.submit)
        self.lb3 = QLabel(self)
        self.lb3.setStyleSheet('color: red')

        # --- display all elements
        layout.addRow(self.pb)
        layout.addRow(self.lb1)
        layout.addRow(self.lb2)
        layout.addRow(self.cb)
        layout.addRow('Submit?', self.btn3)
        layout.addRow(self.lb3)

    def tab_5(self):
        layout = QFormLayout()
        self.tab5.setLayout(layout)

        # --- add all elements
        self.pb = QProgressBar(self)
        self.pb.setValue(100)
        self.lb = QLabel(self)
        self.lb.setText("All done! Thank you for applying!")

        # --- display all elements
        layout.addRow(self.pb)
        layout.addRow(self.lb)

    def nextTab(self):
        print(self.currentIndex())
        self.setCurrentIndex(self.currentIndex() + 1)

    def submit(self):
        if self.cb.isChecked():
            self.setCurrentIndex(self.currentIndex() + 1)
            self.lb3.setText("")
        else:
            self.lb3.setText("YOU NEED TO AGREE TO OUR TERMS BEFORE USING THE ULTIMATE GUI!")


# --- main program
app = QApplication(sys.argv)
ex = Ultimate()
ex.show()
sys.exit(app.exec_())
