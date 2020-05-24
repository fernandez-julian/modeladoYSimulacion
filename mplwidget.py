from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import random
from pvi import *


class MplWidget(QWidget):

    global data
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        #data = [random.random() for i in range(10)]

        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        #self.canvas.axes.plot(data, '*-')

    def recalculateData(self,idex, funcion, xi, ti, tf, h):

        self.canvas.axes.clear()
        if (idex == 0):
            MplWidget.data = euler(xi, ti, tf, h, funcion)
            self.canvas.axes.plot(MplWidget.data[0], MplWidget.data[1], '*-')
        if (idex == 1):
            MplWidget.data = euler_mejorado(xi, ti, tf, h, funcion)
            self.canvas.axes.plot(MplWidget.data[0], MplWidget.data[1], '*-', label='Predicto')
            self.canvas.axes.plot(MplWidget.data[0], MplWidget.data[2], '*-', label='Corrector')
            leg = self.canvas.axes.legend(loc="upper left")
            #leg = self.canvas.axes.legend(loc=2, bbox_to_anchor=(1.05, 1.0))
        if (idex == 2):
            MplWidget.data = rungeKutta(xi, ti, tf, h, funcion)
            self.canvas.axes.plot(MplWidget.data[0], MplWidget.data[1], '*-')

        self.canvas.draw()
