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
                             QVBoxLayout) 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import random, sys, re, string

# Create the QWidget class and initiate the objects inside
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Account")
        self.setWindowIcon(QIcon(r'img/market.png'))
        self.setGeometry(650, 300, 400, 300)
        self.setMaximumWidth(400)
        self.setMaximumHeight(300)
        
        # Add customer font to array, ready to be loaded to any text object
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font < 0 :
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        # Init the main horizontal layout
        main_horizontal_layout = QHBoxLayout()
        main_horizontal_layout.addStretch()
        main_horizontal_layout.addSpacing(2)

        # Init the left vertical layout, containing the QLabels objects
        left_vertical_layout = QVBoxLayout()
        left_vertical_layout.addStretch()
        left_vertical_layout.addSpacing(2)

        first_name = QLabel()
        first_name.setText("First Name")
        first_name.setFont(QFont(fonts[0], 12))
        first_name.setAlignment(Qt.AlignLeft)

        # Add the objects to the left vertical objects
        left_vertical_layout.addWidget(first_name)

        # Init the right vertical layout, containing the QLineEdit objects
        right_vertical_layout = QVBoxLayout()
        right_vertical_layout.addStretch()
        right_vertical_layout.addSpacing(2)

        first_name_textbox = QLineEdit()
        first_name_textbox.setFont(QFont(fonts[0], 12))
        first_name_textbox.setFixedWidth(300)
        first_name_textbox.setAlignment(Qt.AlignRight)


        # Add the object to the right vertical layout
        right_vertical_layout.addWidget(first_name_textbox)

        # Add right and left layout to the main horizontal layout
        main_horizontal_layout.addLayout(left_vertical_layout)
        main_horizontal_layout.addLayout(right_vertical_layout)

        # Init the Main Layout which loads all objects above
        main_layout = QVBoxLayout()
        main_layout.addLayout(main_horizontal_layout)
        self.setLayout(main_layout)
        self.show()



def init_app():
    app = QApplication(sys.argv)
    window = Register()
    window.show()
    app.exec()

init_app()
