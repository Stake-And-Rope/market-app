#!/usr/bin/python3
import sys
sys.path.append(r'..')
from PyQt5.QtWidgets import (
                            QVBoxLayout,
                            QHBoxLayout,
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
from db_handle import postgres_conn
import register
import main_menu



class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LogIn Window")
        self.setWindowIcon(QIcon(r'../img/login.png'))
        self.setGeometry(650, 300, 400, 150)
        self.setMaximumWidth(400)
        self.setMaximumHeight(150)

        """Add custom font to array, ready to be loaded to any text object"""
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
        create_an_account_button.clicked.connect(lambda : open_register())
        create_an_account_button.setText("Create an account")
        create_an_account_button.setFont(QFont("Arial", 9))
        create_an_account_button.setFlat(True)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(new_user_label)
        title_layout.addWidget(create_an_account_button)

        """INIT THE FIRST CENTERED VERTICAL LAYOUT"""
        first_center_vertical_layout = QVBoxLayout()

        username_label = QLineEdit()
        username_label.setPlaceholderText("Username")
        username_label.setStyleSheet("""
            QLineEdit {
                width: 100%;
                height: 40px;
                font-size: 16px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
                margin-bottom: 10px;
            }
        """)

        password_label = QLineEdit()
        password_label.setPlaceholderText("Password")
        password_label.setEchoMode(QLineEdit.Password)
        password_label.setStyleSheet("""
            QLineEdit {
                width: 100%;
                height: 40px;
                font-size: 16px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
        """)
        
        log_in_button = QPushButton("Log in")
        log_in_button.clicked.connect(lambda : login())
        log_in_button.setStyleSheet("""
            QPushButton {
                width: 100%;
                height: 40px;
                font-size: 14px;
                font-weight: bold;
                background-color: #3ca9e2;
                color: #fff;
                border: none;
                border-radius: 4px;
                margin-top: 10px;
                padding: 0;
            }
            QPushButton:hover {
                background-color: #329dd5;
            }
        """)

        """ADD LABEL TO THE CENTERED VERTICAL LAYOUT"""
        first_center_vertical_layout.addWidget(username_label)
        first_center_vertical_layout.addWidget(password_label)
        first_center_vertical_layout.addWidget(log_in_button)

        """INIT THE MAIN LAYOUT"""
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addLayout(first_center_vertical_layout)
        self.setLayout(main_layout)
        self.show()
        
        def login():
            try:
                postgres_conn.customer_client(username_label.text(), password_label.text())
                postgres_conn.customer_client(username_textbox.text(), password_textbox.text())
                open_main_menu()
            except (Exception) as error:
                error_msg_box = QMessageBox(self)
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg_box.setText("Wrong username and/or password!")
                error_msg_box.setWindowTitle("LoigIn unsuccessfull")
                error_msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box = error_msg_box.exec()
        
        def open_register():
            register.start_window()
            login_window.hide()
            
        def open_main_menu():
            main_menu.start_window()
            login_window.hide()
            
def init_app():
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('styles.qss').read_text())
    global login_window
    login_window = LogIn()
    login_window.show()
    app.exec()

def start_window():
    global login_window
    login_window = LogIn()
    login_window.show()



    

# init_app()