import sys

from PyQt5.QtWidgets import (
                            QVBoxLayout,
                            QWidget,
                            QLabel,
                            QHBoxLayout,
                            QPushButton,
                            QApplication,
                            QLabel,
                            QMainWindow
                            )

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LogIn Window")
        self.setWindowIcon(QIcon(r'../img/login.png'))
        self.setGeometry(650, 300, 400, 250)
        self.setMaximumWidth(400)
        self.setMaximumHeight(250)

        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font >= 0:
            fonts = QFontDatabase.applicationFontFamilies(font)
        else:
            print("Error loading fonts!")

        """Init the main vertical layout"""
        main_layout = QVBoxLayout()
        second_main_vertical_layout = QVBoxLayout()

        """Init the first center vertical layout"""
        first_center_vertical_layout = QVBoxLayout()

        title_label = QLabel()
        title_label.setText("Log In")
        title_label.setFont(QFont(fonts[0], 23))
        title_label.setAlignment(Qt.AlignCenter)

        new_user_label = QLabel()
        new_user_label.setText("New user?" + '\u0332'.join(" Create an account"))
        new_user_label.setFont(QFont(fonts[0], 9))
        new_user_label.setAlignment(Qt.AlignCenter)
        new_user_label.setStyleSheet("color: #003366")

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

        """Add labels to the center vertical layout"""
        first_center_vertical_layout.addWidget(title_label)
        first_center_vertical_layout.addWidget(new_user_label)
        first_center_vertical_layout.addWidget(username_label)
        first_center_vertical_layout.addWidget(username_textbox)
        first_center_vertical_layout.addWidget(password_label)
        first_center_vertical_layout.addWidget(password_textbox)


        """Init the second center horizontal layout - the buttons"""
        two_buttons_layout = QHBoxLayout()

        # sign_in_button = QPushButton()
        # sign_in_button.setText("Sign in")
        # sign_in_button.setFont(QFont('Arial', 8))

        log_in_button = QPushButton()
        log_in_button.setText("Log in")
        log_in_button.setFont(QFont(fonts[0], 11))
        log_in_button.setStyleSheet("background-color : lightBlue")

        """Add buttons to the buttons layout"""
        # two_buttons_layout.addWidget(sign_in_button)
        two_buttons_layout.addWidget(log_in_button)

        """Add the two layouts in the one layout - the second main vertical layout"""
        second_main_vertical_layout.addLayout(first_center_vertical_layout)
        second_main_vertical_layout.addLayout(two_buttons_layout)

        """Init the Main Layout"""
        main_layout.addLayout(second_main_vertical_layout)
        self.setLayout(main_layout)
        self.show()


app = QApplication(sys.argv)
login_window = LogIn()
login_window.show()
app.exec()