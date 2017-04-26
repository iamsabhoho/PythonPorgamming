import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QProgressBar,\
    QDockWidget, QCalendarWidget, QLabel, QTabWidget, QComboBox, QLineEdit, QFormLayout

class Ultimate(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(600, 400, 700, 500)
        self.setWindowTitle('Taekwondo Registration')

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, "Registration")
        self.addTab(self.tab2, "Choose your form")
        self.addTab(self.tab3, "Done")

        self.tab_1()
        self.tab_2()
        self.tab_3()

        self.show()

    def tab_1(self):
        layout = QFormLayout()
        self.tab1.setLayout(layout)
        self.pb = QProgressBar(self)
        self.pb.setValue(0)
        self.txt1 = QLineEdit(self)
        self.txt1.setPlaceholderText("Sabrina")
        self.txt2 = QLineEdit(self)
        self.txt2.setPlaceholderText("Ho")
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 50)
        self.dock1 = QDockWidget('Select your birthday', self)
        self.dock1.setWidget(self.cal)
        self.dock1.move(105, 120)
        self.dock1.setFloating(False)
        self.dock1.setFeatures(self.dock1.DockWidgetClosable | self.dock1.DockWidgetMovable)
        self.dock1.setFeatures(self.dock1.NoDockWidgetFeatures)
        self.btn = QPushButton('->', self)
        self.btn.clicked.connect(self.nextTab)
        self.label1 = QLabel(self)
        layout.addRow(self.pb)
        layout.addRow('First Name', self.txt1)
        layout.addRow('Last Name', self.txt2)
        layout.addRow(self.label1)
        layout.addWidget(QLabel("Gender"))
        layout.addWidget(QCheckBox("Male"))
        layout.addWidget(QCheckBox("Female"))
        layout.addRow('Birthday', self.dock1)
        layout.addRow('Next Section', self.btn)




    def tab_2(self):
        layout = QFormLayout()
        self.tab2.setLayout(layout)
        self.pb = QProgressBar(self)
        self.pb.setValue(50)
        self.lb = QLabel(self)
        self.cb = QComboBox(self)
        self.cb.addItem("1")
        self.cb.addItem("2")
        self.cb.addItem("3")
        self.cb.addItem("4")
        self.cb.addItem("5")
        self.cb.addItem("6")
        self.cb.addItem("7")
        self.cb.addItem("8")
        self.btn1 = QPushButton('->', self)
        self.btn1.clicked.connect(self.nextTab)
        layout.addRow(self.pb)
        layout.addRow('Choose form:', self.cb)
        layout.addRow('Next Section', self.btn1)

    def tab_3(self):
        layout = QFormLayout()
        self.tab3.setLayout(layout)
        self.pb = QProgressBar(self)
        self.pb.setValue(100)
        self.lb = QLabel(self)
        self.lb.setText("You are now done with the registration ;)")
        layout.addRow(self.pb)
        layout.addRow(self.lb)

    def nextTab(self):
        print(self.currentIndex())
        self.setCurrentIndex(self.currentIndex() + 1)

# --- main program
app = QApplication(sys.argv)
ex = Ultimate()
ex.show()
sys.exit(app.exec_())
