#!/usr/bin/python3

"""IMPORT QT FRAMEWORK"""
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QLineEdit,
    QMessageBox,
    QApplication
)

from PyQt5.QtGui import (
    QIcon,
    QFontDatabase,
    QFont
)
from PyQt5.QtCore import Qt
from pathlib import Path
from collections import deque

"""DIRECTORY IMPORTS"""
import sys
sys.path.append(r'..')
from db_handle import postgres_conn
import register, main_menu



class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LogIn Window")
        self.setWindowIcon(QIcon(r'../img/login.png'))
        self.setGeometry(650, 300, 400, 150)
        self.setMaximumWidth(400)
        self.setMaximumHeight(150)
        
        """ADMIN CLIENT TO THE POSTGRE DATABASE"""
        admin_cursor = postgres_conn.POSTGRES_CURSOR
        admin_connection = postgres_conn.POSTGRES_CONNECTION

        """ADD CUSTOM FONTS"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font >= 0:
            fonts = QFontDatabase.applicationFontFamilies(font)
        else:
            print("Error loading fonts!")

        """INIT THE TITLE LAYOUT"""
        title_layout = QVBoxLayout()
        title_label = QLabel()
        title_label.setText("Log In")
        title_label.setFont(QFont("Arial", 23))
        title_label.setAlignment(Qt.AlignCenter)

        new_user_label = QLabel()
        new_user_label.setText("New user?")
        new_user_label.setFont(QFont("Arial", 9))
        new_user_label.setAlignment(Qt.AlignCenter)
        new_user_label.setStyleSheet("color: #003366")

        create_an_account_button = QPushButton()
        create_an_account_button.clicked.connect(lambda: open_register())
        create_an_account_button.setText("Create an account")
        create_an_account_button.setFont(QFont("Arial", 9))
        create_an_account_button.setFlat(True)

        title_layout.addWidget(title_label)
        title_layout.addWidget(new_user_label)
        title_layout.addWidget(create_an_account_button)

        """INIT THE FIRST CENTERED VERTICAL LAYOUT"""
        first_center_vertical_layout = QVBoxLayout()
        user_texts = deque(["Username", "Password"])

        user_data = []
        for i in range(2):
            current_label = QLineEdit()
            current_label.setPlaceholderText(user_texts.popleft())
            current_label.setFont(QFont("Arial", 9))
            current_label.setProperty("class", "username_label")
            if i == 1:
                current_label.setEchoMode(QLineEdit.Password)
            user_data.append(current_label)
            first_center_vertical_layout.addWidget(current_label)
        print(user_data[0].text(), user_data[1].text())

        log_in_button = QPushButton("Log in")
        log_in_button.clicked.connect(lambda: login())
        log_in_button.setProperty("class", "login_register_button")

        """ADD LABEL TO THE CENTERED VERTICAL LAYOUT"""
        first_center_vertical_layout.addWidget(log_in_button)

        """INIT THE MAIN LAYOUT"""
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addLayout(first_center_vertical_layout)
        self.setLayout(main_layout)
        self.show()

        def login():
            try:
                postgres_conn.user_client(user_data[0].text(), user_data[1].text())
                global user_cursor, user_connection
                user_cursor = postgres_conn.USER_POSTGRES_CURSOR
                user_connection = postgres_conn.USER_POSTGRES_CONNECTION
                open_main_menu()
            except (Exception) as error:
                error_msg_box = QMessageBox(self)
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg_box.setText("Wrong username and/or password!")
                error_msg_box.setWindowTitle("LogIn unsuccessfull")
                error_msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box = error_msg_box.exec()



"""INIT THE MAIN APP - THIS FUNCTION IS USED IN MAIN TO OPEN THE LOGIN"""
def init_app():
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('styles.qss').read_text())
    global login_window
    login_window = LogIn()
    login_window.show()
    app.exec()

"""OPENS THE LOGIN MENU - USED TO GO BACK FROM REGISTER OR WHEN USER IS LOGGING OUT"""
def start_window():
    global login_window
    login_window = LogIn()
    login_window.show()
    
"""OPENS THE REGISTER MENU"""
def open_register():
    register.start_window()
    login_window.hide()

"""OPENS THE MAIN MENU WINDOW"""
def open_main_menu():
    main_menu.start_window()
    login_window.hide()
