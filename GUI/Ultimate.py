import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QProgressBar,\
    QDockWidget, QCalendarWidget, QLabel, QTabWidget, QComboBox, QLineEdit, QFormLayout

qss = 'QWidget{background-color: rgb(50, 50, 50);}' \
      'QLineEdit{color: white;}' \
      'QLineEdit#grade{background-color: rgb(150, 150, 150);' \
      'font: 100 14pt bold "Courier";' \
      'border: 2px;' \
      'color:white;}'

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
        self.addTab(self.tab2, "Choose sparring/poomsae")
        self.addTab(self.tab3, "Done")

        self.tab_1()
        self.tab_2()
        self.tab_3()

        self.setStyleSheet(qss)

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
        self.cb1 = QComboBox(self)

        self.cb1.addItem("Flyweight")
        self.cb1.addItem("Featherweight")
        self.cb1.addItem("Welterweight")
        self.cb1.addItem("Heavyweight")

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

        layout.addWidget(QLabel("Sparring or Poomsae?"))
        layout.addWidget(QCheckBox("Sparring"))
        layout.addWidget(QCheckBox("Poomsae"))

        layout.addRow('Choose weight:', self.cb1)
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

        # --- read information from other two tabs
        # --- use dictionary




    def nextTab(self):
        print(self.currentIndex())
        self.setCurrentIndex(self.currentIndex() + 1)

# --- main program
app = QApplication(sys.argv)
ex = Ultimate()
ex.show()
sys.exit(app.exec_())
