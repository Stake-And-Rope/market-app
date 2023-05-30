#!/usr/bin/python3
import sys
sys.path.append('..')

# Import PyQt5 Engine
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QGridLayout,
                             QLabel,
                             QFrame,
                             QGroupBox,
                             QLineEdit,
                             QMessageBox,
                             QPlainTextEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect,
                             )

from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UpdateAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update User Account")
        self.setWindowIcon(QIcon(r'../img/market.png'))