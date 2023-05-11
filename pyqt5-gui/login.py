from PyQt5.QtWidgets import (
                            QVBoxLayout,
                            QHBoxLayout,
                            QPushButton,
                            QLabel
                            )

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
sys.path.append(r'..')
from db_handle import postgres_conn
import register


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

        """Init the title layout"""
        title_layout = QVBoxLayout()
        
        title_label = QLabel()
        title_label.setText("Log In")
        title_label.setFont(QFont(fonts[0], 23))
        title_label.setAlignment(Qt.AlignCenter)
        
        new_user_label = QLabel()
        new_user_label.setText("New user?")
        new_user_label.setFont(QFont(fonts[0], 9))
        new_user_label.setAlignment(Qt.AlignCenter)
        new_user_label.setStyleSheet("color: #003366")
        
        create_an_account_button = QPushButton()
        create_an_account_button.clicked.connect(lambda : open_register())
        create_an_account_button.setText("Create an account")
        create_an_account_button.setFont(QFont(fonts[0], 9))
        create_an_account_button.setFlat(True)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(new_user_label)
        title_layout.addWidget(create_an_account_button)

        """Init the first center vertical layout"""
        first_center_vertical_layout = QVBoxLayout()

        username_label = QLabel()
        username_label.setText("Username")
        username_label.setFont(QFont(fonts[0], 12))

        username_textbox = QLineEdit()
        username_textbox.setFont(QFont(fonts[0], 11))

        password_label = QLabel()
        password_label.setText("Password")
        password_label.setFont(QFont(fonts[0], 12))

        password_textbox = QLineEdit()
        password_textbox.setFont(QFont(fonts[0], 11))
        password_textbox.setEchoMode(QLineEdit.Password)
        
        log_in_button = QPushButton()
        log_in_button.clicked.connect(lambda : login())
        log_in_button.setText("Log in")
        log_in_button.setFont(QFont(fonts[0], 11))
        log_in_button.setStyleSheet("background-color : lightBlue")

        """Add labels to the center vertical layout"""
        first_center_vertical_layout.addWidget(username_label)
        first_center_vertical_layout.addWidget(username_textbox)
        first_center_vertical_layout.addWidget(password_label)
        first_center_vertical_layout.addWidget(password_textbox)
        first_center_vertical_layout.addWidget(log_in_button)

        """Init the Main Layout"""
        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addLayout(first_center_vertical_layout)
        self.setLayout(main_layout)
        self.show()
        
        def login():
            try:
                postgres_conn.customer_client(username_textbox.text(), password_textbox.text())
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
            
def init_app():
    app = QApplication(sys.argv)
    global login_window
    login_window = LogIn()
    login_window.show()
    app.exec()

def start_window():
    global login_window
    login_window = LogIn()
    login_window.show()

def open_user_registration(user):
    return f"You clicked me, {user}!"
# init_app()