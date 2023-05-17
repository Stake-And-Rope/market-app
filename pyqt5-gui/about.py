import sys

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QApplication
)
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(650, 300, 500, 300)


app = QApplication(sys.argv)
about_window = About()
about_window.show()
app.exec_()