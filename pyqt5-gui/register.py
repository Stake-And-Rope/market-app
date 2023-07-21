#!/usr/bin/python3
import sys
sys.path.append(r'..')

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
from db_handle import postgres_conn, register_user
import login
import random, re
from collections import deque

"""Create the QWidget class and initiate the objects inside"""

"""CREATE THE QWIDGET CLASS AND INIT THE OBJECTS"""

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Account")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(650, 300, 400, 500)
        self.setMaximumWidth(400)
        self.setMaximumHeight(500)

        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font < 0 :
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        """INIT THE TOP IMAGE LAYOUT"""
        image_layout = QVBoxLayout()
        image_layout.addStretch()
        image_layout.addSpacing(2)
        image_widget = QLabel()
        image_widget.setText("Image will appear here")
        pixmap = QPixmap(r'../img/store-banner2.png')
        image_widget.setPixmap(pixmap)
        image_widget.resize(self.width(), self.height())
        image_widget.setScaledContents(True)
        
        image_layout.addWidget(image_widget)

        """INIT THE MAIN HORIZONTAL LAYOUT"""
        main_horizontal_layout = QHBoxLayout()
        main_horizontal_layout.addStretch()
        main_horizontal_layout.addSpacing(2)
        
        qlabels_list = []
        qlineedit_list = []

        """Init the labels, containing textboxes in them"""
        form_layout = QVBoxLayout()

        name_layout = QHBoxLayout()
        name_layout_texts = deque(["First name", "Last name"])
        for i in range(2):
            current_label = QLineEdit()
            current_label.setText(name_layout_texts.popleft())
            current_label.setProperty("class", "usernamelabel")
        
            name_layout.addWidget(current_label)

        form_layout.addLayout(name_layout)

        user_name_label = QLineEdit()
        user_name_label.setProperty("class", "usernamelabel")
        user_name_label.setText("Username")
        user_name_label.setProperty("class", "usernamelabel")
        form_layout.addWidget(user_name_label)

        phone_number_label = QLineEdit()
        phone_number_label.setText("Phone Number")
        phone_number_label.setProperty("class", "usernamelabel")
        form_layout.addWidget(phone_number_label)

        email_address_label = QLineEdit()
        email_address_label.setText("Email Address")
        email_address_label.setProperty("class", "usernamelabel")
        form_layout.addWidget(email_address_label)
        
        """Password Label is initialized two times"""

        password_label = QLineEdit()
        password_label.setText("Password")
        password_label.setEchoMode(QLineEdit.Password)
        password_label.setProperty("class", "usernamelabel")
        form_layout.addWidget(password_label)

        password_label_repeat = QLineEdit()
        password_label_repeat.setText("Repeat Password")
        password_label_repeat.setEchoMode(QLineEdit.Password)
        password_label_repeat.setProperty("class", "usernamelabel")
        form_layout.addWidget(password_label_repeat)
        

        """BUTTONS LAYOUT"""
        buttons_layout = QHBoxLayout()

        register_button = QPushButton()
        register_button.setGeometry(50, 50, 200, 50)
        register_button.setProperty("class", "buttons")
        register_button.clicked.connect(lambda : create_new_account())
        register_button.setText('Register')
        register_button.setFont(QFont("Arial", 12))

        back_button = QPushButton()
        back_button.clicked.connect(lambda: open_login())
        back_button.setText('Back')
        back_button.setFont(QFont("Arial", 12))
        back_button.setProperty("class", "buttons")

        buttons_layout.addWidget(register_button)
        buttons_layout.addWidget(back_button)

        """INIT THE MAIN LAYOUT """
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(main_horizontal_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(image_layout)
        self.setLayout(main_layout)
        self.show()

        def create_new_account():
            # Insert code here
            """This function should verify the user data and execute series of queries to create the new user inside the DB"""
            create_account_errors = []
            while True:
                user_id = [str(random.randint(0, 9)) for x in range(10)]
                user_id = ''.join(user_id)
                postgres_conn.admin_client()
                postgres_conn.POSTGRES_CURSOR.execute(f"SELECT customer_id FROM customers WHERE customer_id = {user_id}")
                current_ids = postgres_conn.POSTGRES_CURSOR.fetchall()
                if user_id not in current_ids:
                    break
            
            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT username FROM customers WHERE username = '{user_name_label.text()}'")
            if postgres_conn.POSTGRES_CURSOR.fetchall():
                create_account_errors.append('Username already exists')
            
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if not re.match(email_pattern, email_address_label.text()):
                create_account_errors.append('Incorect email address')

            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT email_address FROM customers WHERE email_address = '{email_address_label.text()}'")
            if postgres_conn.POSTGRES_CURSOR.fetchall():
                create_account_errors.append('Email address already existing')

            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT phone FROM customers WHERE phone = '{phone_number_label.text()}'")
            if postgres_conn.POSTGRES_CURSOR.fetchall():
                create_account_errors.append('Phone number already exists')
                
            if password_label.text() != password_label_repeat.text():
                create_account_errors.append('Password fields does not match.')
            if len(password_label.text()) < 8:
                create_account_errors.append('Password is too short. It must be at least 8 characters.')
            if not re.search(re.compile('[!@#$%^&*()-+?_=,<>/]'), password_label.text()):
                create_account_errors.append("Password must contain at least one special character.")
            if not re.search(re.compile('[A-Z]'), password_label.text()):
                create_account_errors.append("Password must contain at least one uppercase letter.")
            if not re.search(re.compile('[0-9]'), password_label.text()):
                create_account_errors.append("Password must contain at least one number.")
            
            if len(create_account_errors) == 0:
                    """Create new record inside customers table"""
                    postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO customers (customer_id, username, first_name, last_name, email_address, phone) \
                                                          VALUES ({user_id}, '{user_name_label.text().lower()}', '{first_name_label.text()}', '{last_name_label.text()}',\
                                                              '{email_address_label.text()}', '{phone_number_label.text()}')")
                    register_user.create_user(user_name_label.text(), password_label.text())
            else:
                error_msg_box = QMessageBox(self)
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg = '\n'.join(create_account_errors)
                error_msg_box.setText(error_msg)
                error_msg_box.setWindowTitle("Error during creating new account")
                error_msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box = error_msg_box.exec()
                
        def open_login():
            login.start_window()
            register_window.hide()
                    
def start_window():
    global register_window
    register_window = Register()
    register_window.show()

# init_app()
