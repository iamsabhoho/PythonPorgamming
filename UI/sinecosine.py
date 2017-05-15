import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time

class Sine(QDockWidget):
    def __init__(self, parent=None):
        super(Sine, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.hostPlot = QtWidgets.QWidget(self)
        self.hostPlot.setObjectName("hostPlot")
        self.hostPlot.setSizePolicy(QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Maximum)
        self.hostPlot.setMinimumSize(500,200)
        self.grPlot = PlotWidget(self)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.grPlot.setObjectName("grPlot")
        self.grPlot.raise_()
        self.grPlot.raise_()
        self.grPlot.raise_()

        self.btnAdd = QtWidgets.QPushButton(self)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.setText("Refresh")

        self.verticalLayout = QVBoxLayout(self.hostPlot)
        self.verticalLayout.addWidget(self.grPlot)
        self.verticalLayout.addWidget(self.btnAdd)

    def resizeEvent(self, e):
        self.hostPlot.setGeometry(10,10, e.size().width(), e.size().height())
        self.grPlot.setGeometry(10,10, e.size().width(), 0.9*e.size().height())
        print('resized')

    def plot(self, data):
        X = data['X']
        Y = data['Y']
        pen = data['pen']
        self.grPlot.plot()


class Cosine(QDockWidget):
    def __init__(self, parent=None):
        super(Cosine, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.hostPlot = QtWidgets.QWidget(self)
        self.hostPlot.setObjectName("hostPlot")
        self.hostPlot.setSizePolicy(QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Maximum)
        self.hostPlot.setMinimumSize(500,200)
        self.grPlot = PlotWidget(self)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.grPlot.setObjectName("grPlot")
        self.grPlot.raise_()
        self.grPlot.raise_()

        self.verticalLayout = QVBoxLayout(self.hostPlot)
        self.verticalLayout.addWidget(self.grPlot)

    def resizeEvent(self, e):
        self.hostPlot.setGeometry(10,10, e.size().width(), e.size().height())
        self.grPlot.setGeometry(10,10, e.size().width(), 0.9*e.size().height())

    def hist(self, data):
        Y = data['Y']
        pen = data['pen']
        y, x = np.histogram(Y)
        self.grPlot.clear()
        self.grPlot.plot()

class SinCo(QDockWidget):
    def __init__(self, parent=None):
        super(SinCo, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.hostPlot = QtWidgets.QWidget(self)
        self.hostPlot.setObjectName("hostPlot")
        self.hostPlot.setSizePolicy(QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Maximum)
        self.hostPlot.setMinimumSize(500,200)
        self.grPlot = PlotWidget(self)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.grPlot.setObjectName("grPlot")
        self.grPlot.raise_()
        self.grPlot.raise_()

        self.verticalLayout = QVBoxLayout(self.hostPlot)
        self.verticalLayout.addWidget(self.grPlot)

    def resizeEvent(self, e):
        self.hostPlot.setGeometry(10,10, e.size().width(), e.size().height())
        self.grPlot.setGeometry(10,10, e.size().width(), 0.9*e.size().height())

    def hist(self, data):
        Y = data['Y']
        pen = data['pen']
        y, x = np.histogram(Y)
        self.grPlot.clear()
        self.grPlot.plot()

class SandboxApp(QtWidgets.QApplication):
    def __init__(self, *args, **kwargs):
        super(SandboxApp, self).__init__(*args)
        self.mainwindow = MainWindow()
        self.mainwindow.setGeometry(50,100,1200,600)
        self.mainwindow.show()
        self.mainwindow.setContextMenuPolicy(Qt.NoContextMenu)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.SineD = Sine()
        self.CosineD = Cosine()
        self.SinCoD = SinCo()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.SineD)
        self.addDockWidget(Qt.RightDockWidgetArea, self.CosineD)
        self.addDockWidget(Qt.RightDockWidgetArea, self.SinCoD)
        self.update()

    def update(self):
        t = np.arange(0 , 20, 20/2000)
        i = 0.1
        s = np.sin(2 * np.pi * t + i)
        c = np.cos(2 * np.pi * t + i)

        C=pt.hsvColor(time.time()/5%1,alpha=.5)
        pen=pt.mkPen(color=C,width=2)
        data = {'X':s, 'Y':c, 'pen':pen}
        self.SineD.plot(data)
        self.CosineD.hist(data)
        self.SinCoD.hist(data)
        QtCore.QTimer.singleShot(100, self.update) # QUICKLY repeat

def main():
    app = SandboxApp(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
