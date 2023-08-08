#!/usr/bin/python3

# Import PyQt5 Engine 
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QMessageBox,
                             QHBoxLayout,
                             QVBoxLayout)

from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
sys.path.append(r'..')
from db_handle import postgres_conn, register_user
import login
import random, re
from collections import deque

admin_cursor = postgres_conn.POSTGRES_CURSOR
admin_connection = postgres_conn.POSTGRES_CONNECTION

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
        if font < 0:
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

        font = QFont("Arial", 12)

        """INIT THE LABELS FOR THE TEXTBOXES"""
        form_layout = QVBoxLayout()
        name_layout = QHBoxLayout()
        name_layout_texts = deque(["First name", "Last name"])
        user_data_one = [] # Holds the firts name and last name QLineEdit's
        for i in range(2):
            current_label = QLineEdit()
            current_label.setPlaceholderText(name_layout_texts.popleft())
            current_label.setFont(font)
            current_label.setProperty("class", "username_label")
            user_data_one.append(current_label)
            name_layout.addWidget(current_label)
        form_layout.addLayout(name_layout)

        other_important_texts = deque(["Username", "Phone Number", "Email Address", "Password", "Repeat Password"])
        user_data_two = [] # Holds rest of the user data during the registration
        for i in range(5):
            current_label = QLineEdit()
            current_label.setPlaceholderText(other_important_texts.popleft())
            current_label.setFont(font)
            current_label.setProperty("class", "username_label")
            if i >= 3:
                current_label.setEchoMode(QLineEdit.Password)
            user_data_two.append(current_label)
            form_layout.addWidget(current_label)

        """BUTTONS LAYOUT"""
        buttons_layout = QHBoxLayout()
        buttons_layout_texts = deque(["Register", "Back"])
        for i in range(2):
            current_label = QPushButton(buttons_layout_texts.popleft())
            current_label.setFont(font)
            if i == 0:
                current_label.setProperty("class", "login_register_button")
                current_label.clicked.connect((lambda: create_new_account()))
            else:
                current_label.setProperty("class", "back_button")
                current_label.clicked.connect(lambda: open_login())
            buttons_layout.addWidget(current_label)

        """INIT THE MAIN LAYOUT """
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(main_horizontal_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addLayout(image_layout)
        self.setLayout(main_layout)
        self.show()

        def create_new_account():
            create_account_errors = []
            while True:
                user_id = [str(random.randint(0, 9)) for x in range(10)]
                user_id = ''.join(user_id)
                admin_cursor.execute(f"SELECT customer_id FROM customers WHERE customer_id = {user_id}")
                existing_ids = admin_cursor.fetchall()
                if user_id not in existing_ids:
                    break

            admin_cursor.execute(f"SELECT username FROM customers WHERE username = '{user_data_two[0].text()}'")
            if admin_cursor.fetchall():
                create_account_errors.append('Username already exists')

            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if not re.match(email_pattern, user_data_two[2].text()):
                create_account_errors.append('Incorect email address')

            admin_cursor.execute(f"SELECT email_address FROM customers WHERE email_address = '{user_data_two[2].text()}'")
            if admin_cursor.fetchall():
                create_account_errors.append('Email address already exists')

            admin_cursor.execute(
                f"SELECT phone FROM customers WHERE phone = '{user_data_two[1].text()}'")
            if admin_cursor.fetchall():
                create_account_errors.append('Phone number already exists')

            if user_data_two[3].text() != user_data_two[4].text():
                create_account_errors.append('Password fields does not match.')
            if len(user_data_two[3].text()) < 8:
                create_account_errors.append('Password is too short. It must be at least 8 characters.')
            if not re.search(re.compile('[!@#$%^&*()-+?_=,<>/]'), user_data_two[3].text()):
                create_account_errors.append("Password must contain at least one special character.")
            if not re.search(re.compile('[A-Z]'), user_data_two[3].text()):
                create_account_errors.append("Password must contain at least one uppercase letter.")
            if not re.search(re.compile('[0-9]'), user_data_two[3].text()):
                create_account_errors.append("Password must contain at least one number.")

            if len(create_account_errors) == 0:
                """Create new record inside customers table"""
                admin_cursor.execute(f"INSERT INTO customers (customer_id, username, first_name, last_name, email_address, phone) \
                                                          VALUES ({user_id}, '{user_data_two[0].text().lower()}', '{user_data_one[0].text()}', '{user_data_one[1].text()}',\
                                                              '{user_data_two[2].text()}', '{user_data_two[1].text()}')")
                register_user.create_user(user_data_two[0].text(), user_data_two[3].text())
                registration_confirm_msg_box = QMessageBox()
                registration_confirm_msg_box.setIcon(QMessageBox.Warning)
                registration_message = 'Congratulations! Your account has been created successfully!'
                registration_confirm_msg_box.setText(registration_message)
                registration_confirm_msg_box.setWindowTitle("Account created successfully!")
                registration_confirm_msg_box.setStandardButtons(QMessageBox.Ok)
                registration_confirm_msg_box.exec()
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

