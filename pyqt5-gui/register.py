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
sys.path.append(r'..')
from db_handle import postgres_conn, register_user
import random, re, string


# Create the QWidget class and initiate the objects inside
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Account")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(650, 300, 400, 500)
        self.setMaximumWidth(400)
        self.setMaximumHeight(500)
        
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

        user_name_label = QLabel()
        user_name_label.setText("User Name")
        user_name_label.setFont(QFont(fonts[0], 12))
        user_name_label.setFixedHeight(25)
        user_name_label.setAlignment(Qt.AlignLeft)
        user_name_label.setStyleSheet("color: #003366")
        qlabels_list.append(user_name_label)   
    
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

        phone_number_label = QLabel()
        phone_number_label.setText("Phone Number")
        phone_number_label.setFont(QFont(fonts[0], 12))
        phone_number_label.setFixedHeight(25)
        phone_number_label.setAlignment(Qt.AlignLeft)
        phone_number_label.setStyleSheet("color: #003366")
        qlabels_list.append(phone_number_label)
        
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
        left_vertical_layout.addWidget(user_name_label)
        left_vertical_layout.addWidget(first_name_label)
        left_vertical_layout.addWidget(last_name_label)
        left_vertical_layout.addWidget(phone_number_label)
        left_vertical_layout.addWidget(email_address_label)
        left_vertical_layout.addWidget(password_label)
        left_vertical_layout.addWidget(password_label_repeat)

        """Init the right vertical layout, containing the QLineEdit objects"""
        right_vertical_layout = QVBoxLayout()
        right_vertical_layout.addStretch()
        right_vertical_layout.addSpacing(2)
        
        user_name_textbox = QLineEdit()
        user_name_textbox.setFont(QFont(fonts[0], 12))
        user_name_textbox.setFixedWidth(300)
        user_name_textbox.setFixedHeight(25)
        user_name_textbox.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(user_name_textbox)
        
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
        
        phone_number_textbox = QLineEdit()
        phone_number_textbox.setFont(QFont(fonts[0], 12))
        phone_number_textbox.setFixedWidth(300)
        phone_number_textbox.setFixedHeight(25)
        phone_number_textbox.setAlignment(Qt.AlignLeft)
        qlineedit_list.append(phone_number_textbox)

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
        right_vertical_layout.addWidget(user_name_textbox)
        right_vertical_layout.addWidget(first_name_textbox)
        right_vertical_layout.addWidget(last_name_textbox)
        right_vertical_layout.addWidget(phone_number_textbox)
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
        register_button.clicked.connect(lambda : create_new_account())
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
            create_account_errors = []
            while True:
                user_id = [str(random.randint(0, 9)) for x in range(10)]
                user_id = ''.join(user_id)
                postgres_conn.admin_client()
                postgres_conn.POSTGRES_CURSOR.execute(f"SELECT customer_id FROM customers WHERE customer_id = {user_id}")
                current_ids = postgres_conn.POSTGRES_CURSOR.fetchall()
                if user_id not in current_ids:
                    break
            
            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT username FROM customers WHERE username = '{user_name_textbox.text()}'")
            if postgres_conn.POSTGRES_CURSOR.fetchall():
                create_account_errors.append('Username already exists')
            
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if not re.match(email_pattern, email_address_textbox.text()):
                create_account_errors.append('Incorect email address')

            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT email_address FROM customers WHERE email_address = '{email_address_textbox.text()}'")
            if postgres_conn.POSTGRES_CURSOR.fetchall():
                create_account_errors.append('Email address already existing')

            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT phone FROM customers WHERE phone = '{phone_number_textbox.text()}'")
            if postgres_conn.POSTGRES_CURSOR.fetchall():
                create_account_errors.append('Phone number already exists')
                
            if password_textbox.text() != password_textbox_repeat.text():
                create_account_errors.append('Password fields does not match.')
            if len(password_textbox.text()) < 8:
                create_account_errors.append('Password is too short. It must be at least 8 characters.')
            if not re.search(re.compile('[!@#$%^&*()-+?_=,<>/]'), password_textbox.text()):
                create_account_errors.append("Password must contain at least one special character.")
            if not re.search(re.compile('[A-Z]'), password_textbox.text()):
                create_account_errors.append("Password must contain at least one uppercase letter.")
            if not re.search(re.compile('[0-9]'), password_textbox.text()):
                create_account_errors.append("Password must contain at least one number.")
            
            print(create_account_errors)
            if len(create_account_errors) == 0:
                    postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO customers (customer_id, username, first_name, last_name, email_address, phone) \
                                                          VALUES ({user_id}, '{user_name_textbox.text().lower()}', '{first_name_textbox.text()}', '{last_name_textbox.text()}',\
                                                              '{email_address_textbox.text()}', '{phone_number_textbox.text()}')")
                    # print('Query Succeeded')
                    #postgres_conn.POSTGRES_CONNECTION.commit()
                    # print('Query Commited')
                    register_user.create_user(user_name_textbox.text(), password_textbox.text())
            else:
                error_msg_box = QMessageBox(self)
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg = '\n'.join(create_account_errors)
                error_msg_box.setText(error_msg)
                error_msg_box.setWindowTitle("Error during creating new account")
                error_msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box = error_msg_box.exec()
                    




def init_app():
    app = QApplication(sys.argv)
    window = Register()
    window.show()
    app.exec()

init_app()
