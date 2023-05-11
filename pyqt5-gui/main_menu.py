#!/usr/bin/python3

# Import PyQt5 Engine 
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLabel, 
                             QLineEdit, 
                             QMessageBox, 
                             QPlainTextEdit, 
                             QHBoxLayout, 
                             QVBoxLayout,
                             QGraphicsDropShadowEffect)

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(200, 150, 1500, 700)
        self.setMaximumWidth(1500)
        self.setMaximumHeight(700)

    

app = QApplication(sys.argv)
global login_window
login_window = MainMenu()
login_window.show()
app.exec()

