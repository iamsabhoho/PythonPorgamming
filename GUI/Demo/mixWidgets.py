#this is a porgram with several widgets taught in class
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QProgressBar,\
    QDockWidget, QCalendarWidget, QLabel, QTabWidget, QComboBox, QLineEdit, QFormLayout, QSpinBox, QHBoxLayout
from PyQt5.QtCore import QDate

class Mix(QTabWidget):
    def __init__(self):
        super(Mix, self).__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.addTab(self.tab1, 'Registration')
        self.addTab(self.tab2, 'Personal Info')
        self.addTab(self.tab3, 'Choosing Forms')
        self.addTab(self.tab4, 'Calender; Check Date') #?

        self.tab_1()
        self.tab_2()
        self.tab_3()
        self.tab_4()

        # -- closing tab
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

    def closeTab(self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def tab_1(self):
        layout = QFormLayout()
        layout.addRow('First Name', QLineEdit())
        self.tab1.setLayout(layout)

    def tab_2(self):
        layout = QFormLayout()
        layout.addRow('First Name', QLineEdit())
        layout.addRow('Last Name', QLineEdit())
        layout.addRow('Gender', QCheckBox()) #set up a checkbox here
        layout.addRow('First Name', QLineEdit())
        layout.addRow('First Name', QLineEdit())
        layout.addRow('First Name', QLineEdit())
        self.tab2.setLayout(layout)

    def tab_3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('Forms'))
        layout.addWidget(QCheckBox('1'))
        layout.addWidget(QCheckBox('2'))
        layout.addWidget(QCheckBox('3'))
        layout.addWidget(QCheckBox('4'))
        layout.addWidget(QCheckBox('5'))
        layout.addWidget(QCheckBox('6'))
        layout.addWidget(QCheckBox('7'))
        layout.addWidget(QCheckBox('8'))
        self.tab3.setLayout(layout)

    #calender
    def tab_4(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.label = QLabel(self)
        date = cal.selectedDate()
        self.label.setText(date.toString())
        self.label.move(20, 200)

    def showDate(self, date):
        self.label.setText(date.toString())


# --- main program
app = QApplication(sys.argv)
ex = Mix()
ex.show()
sys.exit(app.exec_())

#-- adding different functions in different tabs
#-- calender doesnt work




