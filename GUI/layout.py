import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

qss = 'QWidget{background-color: rgb(50, 50, 50);}' \
      'QLineEdit{color: white;}' \
      'QLineEdit#grade{background-color: rgb(150, 150, 150);' \
      'font: 100 14pt bold "Courier";' \
      'border: 2px;' \
      'color:white;}'

class Grades(QWidget):
    def __init__(self):
        super().__init__()

        self.b1 = QLineEdit(self)
        self.b1.setAlignment(Qt.AlignCenter)
        self.b1.setObjectName('value')
        self.b1.setValidator(QIntValidator(0, 100, self))
        self.b1.setPlaceholderText('Enter grade 0-100')
        self.b1.textChanged.connect(self.convert)
        self.b1.setMinimumHeight(50)
        self.b1.setFont(QFont("Arial",20))
        self.setStyleSheet(qss)

        self.b2 = QLineEdit(self)
        self.b2.setText('A+')
        self.b2.setObjectName('grade')
        self.b2.setAlignment(Qt.AlignCenter)
        self.b2.setMinimumHeight(50)
        self.b2.setFont(QFont("Arial", 20))
        self.b2.setEnabled(False)

        self.setWindowTitle("Grade Converter")
        layout = QVBoxLayout()
        layout.addWidget(self.b1)
        layout.addStretch(1)
        layout.addWidget(self.b2)
        self.setLayout(layout)

    def convert(self):
        dictG = {'A+':range(97, 101),
                 'A':range(93, 97),
                 'A-':range(90,93),
                 'B+':range(87,90),
                 'B':range(83,87),
                 'B-':range(80,83),
                 'C+':range(77,80),
                 'C':range(73,77),
                 'C-':range(70,73),
                 'D+':range(67,70),
                 'D':range(63,67),
                 'D-':range(60,63),
                 'F':range(0,60)}
        if self.b1.text() is not '':
            gradeNum = int(self.b1.text())
            for k, d in dictG.items():
                print(gradeNum in d)
                if gradeNum in d:
                    self.b2.setText(k)
                    return
        self.b2.setText('-')


def main():
    app = QApplication(sys.argv)
    ex = Grades()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
