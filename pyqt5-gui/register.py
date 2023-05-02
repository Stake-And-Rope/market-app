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
        self.setWindowIcon(QIcon(r'../img/market.png'))
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

        first_name_label = QLabel()
        first_name_label.setText("First Name")
        first_name_label.setFont(QFont(fonts[0], 12))
        first_name_label.setAlignment(Qt.AlignLeft)

        last_name_label = QLabel()
        last_name_label.setText("Last Name")
        last_name_label.setFont(QFont(fonts[0], 12))
        last_name_label.setAlignment(Qt.AlignLeft)

        email_address_label = QLabel()
        email_address_label.setText("Email Address")
        email_address_label.setFont(QFont(fonts[0], 12))
        email_address_label.setAlignment(Qt.AlignLeft)
        
        # Password Label is initialized two times
        password_label = QLabel()
        password_label.setText("Password")
        password_label.setFont(QFont(fonts[0], 12))
        password_label.setAlignment(Qt.AlignLeft)
        password_label_repeat = QLabel()
        password_label_repeat.setText("Repeat Password")
        password_label_repeat.setFont(QFont(fonts[0], 12))
        password_label_repeat.setAlignment(Qt.AlignLeft)

        # Add the objects to the left vertical objects
        left_vertical_layout.addWidget(first_name_label)
        left_vertical_layout.addWidget(last_name_label)
        left_vertical_layout.addWidget(email_address_label)
        left_vertical_layout.addWidget(password_label)
        left_vertical_layout.addWidget(password_label_repeat)

        # Init the right vertical layout, containing the QLineEdit objects
        right_vertical_layout = QVBoxLayout()
        right_vertical_layout.addStretch()
        right_vertical_layout.addSpacing(2)

        first_name_textbox = QLineEdit()
        first_name_textbox.setFont(QFont(fonts[0], 12))
        first_name_textbox.setFixedWidth(300)
        first_name_textbox.setFixedHeight(25)
        first_name_textbox.setAlignment(Qt.AlignLeft)

        last_name_textbox = QLineEdit()
        last_name_textbox.setFont(QFont(fonts[0], 12))
        last_name_textbox.setFixedWidth(300)
        last_name_textbox.setFixedHeight(25)
        last_name_textbox.setAlignment(Qt.AlignLeft)

        email_address_textbox = QLineEdit()
        email_address_textbox.setFont(QFont(fonts[0], 12))
        email_address_textbox.setFixedWidth(300)
        email_address_textbox.setFixedHeight(25)
        email_address_textbox.setAlignment(Qt.AlignLeft)

        password_textbox = QLineEdit()
        password_textbox.setEchoMode(QLineEdit.Password)
        password_textbox.setFixedWidth(300)
        password_textbox.setFixedHeight(25)
        password_textbox.setAlignment(Qt.AlignLeft)
        password_textbox_repeat = QLineEdit()
        password_textbox_repeat.setEchoMode(QLineEdit.Password)
        password_textbox_repeat.setFixedWidth(300)
        password_textbox_repeat.setFixedHeight(25)
        password_textbox_repeat.setAlignment(Qt.AlignLeft)
        

        # Add the object to the right vertical layout
        right_vertical_layout.addWidget(first_name_textbox)
        right_vertical_layout.addWidget(last_name_textbox)
        right_vertical_layout.addWidget(email_address_textbox)
        right_vertical_layout.addWidget(password_textbox)
        right_vertical_layout.addWidget(password_textbox_repeat)

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
