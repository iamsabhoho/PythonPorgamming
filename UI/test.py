import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time

class MainGraph(QDockWidget):
    def __init__(self, parent=None):
        super(MainGraph, self).__init__(parent=parent)
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
        self.grPlot.plot(X, Y, pen=pen, clear=True)


class HistGraph(QDockWidget):
    def __init__(self, parent=None):
        super(HistGraph, self).__init__(parent=parent)
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
        self.grPlot.plot(x, y, stepMode=True, fillLevel=0, brush=(0,0,255,150))


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
        self.mainD = MainGraph()
        self.histD = HistGraph()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.mainD)
        self.addDockWidget(Qt.RightDockWidgetArea, self.histD)
        self.update()

    def update(self):
        points = 500 #number of data points
        X=np.arange(points)
        Y=np.random.poisson(5, points)
        C=pt.hsvColor(time.time()/5%1,alpha=.5)
        pen=pt.mkPen(color=C,width=2)
        data = {'X':X, 'Y':Y, 'pen':pen}
        self.mainD.plot(data)
        self.histD.hist(data)
        QtCore.QTimer.singleShot(100, self.update) # QUICKLY repeat

def main():
    app = SandboxApp(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
