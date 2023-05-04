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
from db_handle import postgres_conn

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
        
        """Add customer font to array, ready to be loaded to any text object"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font < 0 :
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)
        
        qlabels_list = []
        qlineedit_list = []

        """Init the main horizontal layout"""
        main_horizontal_layout = QHBoxLayout()
        main_horizontal_layout.addStretch()
        main_horizontal_layout.addSpacing(2)
        
        """Init the left vertical layout, containing the qlabels_list objects"""
        left_vertical_layout = QVBoxLayout()
        left_vertical_layout.addStretch()
        left_vertical_layout.addSpacing(2)

        first_name_label = QLabel()
        first_name_label.setText("First Name")
        first_name_label.setFont(QFont(fonts[0], 12))
        first_name_label.setFixedHeight(25)
        first_name_label.setAlignment(Qt.AlignLeft)
        first_name_label.setStyleSheet("color: #003366")
        qlabels_list.append(first_name_label)

        last_name_label = QLabel()
        last_name_label.setText("Last Name")
        last_name_label.setFont(QFont(fonts[0], 12))
        last_name_label.setFixedHeight(25)
        last_name_label.setAlignment(Qt.AlignLeft)
        last_name_label.setStyleSheet("color: #003366")
        qlabels_list.append(last_name_label)

        email_address_label = QLabel()
        email_address_label.setText("Email Address")
        email_address_label.setFont(QFont(fonts[0], 12))
        email_address_label.setFixedHeight(25)
        email_address_label.setAlignment(Qt.AlignLeft)
        email_address_label.setStyleSheet("color: #003366")
        qlabels_list.append(email_address_label)
        
        """Password Label is initialized two times"""
        password_label = QLabel()
        password_label.setText("Password")
        password_label.setFont(QFont(fonts[0], 12))
        password_label.setFixedHeight(25)
        password_label.setAlignment(Qt.AlignLeft)
        password_label.setStyleSheet("color: #003366")
        qlabels_list.append(password_label)
        password_label_repeat = QLabel()
        password_label_repeat.setText("Repeat Password")
        password_label_repeat.setFont(QFont(fonts[0], 12))
        password_label_repeat.setFixedHeight(25)
        password_label_repeat.setAlignment(Qt.AlignLeft)
        password_label_repeat.setStyleSheet("color: #003366")
        qlabels_list.append(password_label_repeat)

        """Apply shadow effect to all QLabel added to qlabels_list array
            shadow variable is customizable"""
        for i in range(len(qlabels_list)):
            shadow = QGraphicsDropShadowEffect()
            shadow.setOffset(2, 1)
            shadow.setColor(QColor(255, 255, 255))
            qlabels_list[i].setGraphicsEffect(shadow)

        """Add the objects to the left vertical objects"""
        left_vertical_layout.addWidget(first_name_label)
        left_vertical_layout.addWidget(last_name_label)
        left_vertical_layout.addWidget(email_address_label)
        left_vertical_layout.addWidget(password_label)
        left_vertical_layout.addWidget(password_label_repeat)

        """Init the right vertical layout, containing the QLineEdit objects"""
        right_vertical_layout = QVBoxLayout()
        right_vertical_layout.addStretch()
        right_vertical_layout.addSpacing(2)

        first_name_textbox = QLineEdit()
        first_name_textbox.setFont(QFont(fonts[0], 12))
        first_name_textbox.setFixedWidth(300)
        first_name_textbox.setFixedHeight(25)
        first_name_textbox.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(first_name_textbox)

        last_name_textbox = QLineEdit()
        last_name_textbox.setFont(QFont(fonts[0], 12))
        last_name_textbox.setFixedWidth(300)
        last_name_textbox.setFixedHeight(25)
        last_name_textbox.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(last_name_textbox)

        email_address_textbox = QLineEdit()
        email_address_textbox.setFont(QFont(fonts[0], 12))
        email_address_textbox.setFixedWidth(300)
        email_address_textbox.setFixedHeight(25)
        email_address_textbox.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(email_address_textbox)

        password_textbox = QLineEdit()
        password_textbox.setEchoMode(QLineEdit.Password)
        password_textbox.setFixedWidth(300)
        password_textbox.setFixedHeight(25)
        password_textbox.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(password_textbox)
        password_textbox_repeat = QLineEdit()
        password_textbox_repeat.setEchoMode(QLineEdit.Password)
        password_textbox_repeat.setFixedWidth(300)
        password_textbox_repeat.setFixedHeight(25)
        password_textbox_repeat.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(password_textbox_repeat)
        
        """Apply shadow effect to qlabels_list array
            shadow variable is customizable"""
        for i in range(len(qlineedit_list)):
            shadow = QGraphicsDropShadowEffect()
            shadow.setOffset(2, 1)
            shadow.setColor(QColor(0, 51, 102))
            qlineedit_list[i].setGraphicsEffect(shadow)
            
        
        """Add the object to the right vertical layout"""
        right_vertical_layout.addWidget(first_name_textbox)
        right_vertical_layout.addWidget(last_name_textbox)
        right_vertical_layout.addWidget(email_address_textbox)
        right_vertical_layout.addWidget(password_textbox)
        right_vertical_layout.addWidget(password_textbox_repeat)

        """Add right and left layout to the main horizontal layout"""
        main_horizontal_layout.addLayout(left_vertical_layout)
        main_horizontal_layout.addLayout(right_vertical_layout)
        
        """Buttons Layout"""
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addSpacing(2)

        register_button = QPushButton()
        register_button.setText('Register')
        register_button.setFont(QFont(fonts[0], 12))

        back_button = QPushButton()
        back_button.setText('Back')
        back_button.setFont(QFont(fonts[0], 12))

        buttons_layout.addWidget(register_button)
        buttons_layout.addWidget(back_button)


        """Init the Main Layout which loads all objects above"""
        main_layout = QVBoxLayout()
        main_layout.addLayout(main_horizontal_layout)
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
        self.show()

        def create_new_account():
            # Insert code here
            """This function should verify the user data and execute series of queries to
                create the new user inside the DB. Consider giving the right read permissions to the new user"""
            while True:
                user_id = str(random.randint(0, 9) for _ in range(10))
                postgres_conn.admin_client()
                postgres_conn.POSTGRES_CURSOR.execute(f"SELECT customer_id FROM customers;")
                current_ids = postgres_conn.POSTGRES_CURSOR.fetchall()
                if user_id not in current_ids:
                    break



def init_app():
    app = QApplication(sys.argv)
    window = Register()
    window.show()
    app.exec()

init_app()
