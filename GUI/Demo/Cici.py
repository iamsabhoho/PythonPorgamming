#QTabWidget
import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QHBoxLayout, QWidget, \
    QFormLayout, QLineEdit, QRadioButton, QCheckBox, QLabel

class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.addTab(self.tab1, 'Contact Details')
        self.addTab(self.tab2, 'Personal Details')
        self.addTab(self.tab3, 'Education Details')
        self.addTab(self.tab4, 'Family Details')

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
        gender = QHBoxLayout()
        gender.addWidget(QRadioButton('Male'))
        gender.addWidget(QRadioButton('Female'))
        layout.addRow(QLabel('Gender'), gender)
        self.tab2.setLayout(layout)

    def tab_3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('Majors'))
        layout.addWidget(QCheckBox('Engineering'))
        layout.addWidget(QCheckBox('Science'))
        self.tab3.setLayout(layout)

    def tab_4(self):
        layout = QFormLayout()
        layout.addRow('Female Guardian:', QLineEdit())
        layout.addRow('Male Guardian:', QLineEdit())
        self.tab4.setLayout(layout)


# --- main program
app = QApplication(sys.argv)
ex = Tab()
ex.show()
sys.exit(app.exec_())
