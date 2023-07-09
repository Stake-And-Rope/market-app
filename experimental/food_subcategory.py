#!/usr/bin/python3
import sys
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
                             QGraphicsOpacityEffect)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
sys.path.append(r'..')

class FoodSubCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Sub Category")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(200, 150, 1500, 700)
        self.setMaximumWidth(1500)
        self.setMaximumHeight(700)

        """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        """CREATE THE USER INFO VERTICAL LAYOUT"""
        user_info_groupbox = QGroupBox('User Information')
        user_info_groupbox.setFont(QFont(fonts[0], 12))
        first_name = QLabel('First Name')
        first_name.setFont(QFont(fonts[0], 12))
        last_name = QLabel('Last Name')
        last_name.setFont(QFont(fonts[0], 12))
        user_info_layout = QVBoxLayout()

        user_info_layout.addWidget(first_name)
        user_info_layout.addWidget(last_name)
        user_info_layout.addStretch(0)
        user_info_layout.addSpacing(100)
        user_info_groupbox.setLayout(user_info_layout)


        """INIT THE MAIN LAYOUT"""
        main_layout = QGridLayout()
        main_layout.addWidget(user_info_groupbox, 0, 0)


        """EXAMINE BELOW TWO LINES HOW EXACTLY THEY APPLY THE LOGIC IN THE UI"""
        main_layout.setRowStretch(1, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)
        self.show()


app = QApplication(sys.argv)
global food_subcategory_window
food_subcategory_window = FoodSubCategory()
food_subcategory_window.show()
app.exec()