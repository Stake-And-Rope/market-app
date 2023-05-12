#!/usr/bin/python3

# Import PyQt5 Engine 
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton,
                             QGridLayout,  
                             QLabel,
                             QFrame,
                             QGroupBox, 
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
from collections import deque

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(200, 150, 1500, 700)
        self.setMaximumWidth(1500)
        self.setMaximumHeight(700)
        
        """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT""" 
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        """CREATE THE USER INFO VERTICAL LAYOUT"""
        user_info_groupbox = QGroupBox('User Information')
        first_name = QLabel('First Name')
        last_name = QLabel('Last Name')
        user_info_layout = QVBoxLayout()

        user_info_layout.addWidget(first_name)
        user_info_layout.addWidget(last_name)
        user_info_layout.addStretch(0)
        user_info_layout.addSpacing(100)
        user_info_groupbox.setLayout(user_info_layout)
        
        """CREATE THE LEFT BUTTONS LAYOUT"""
        left_buttons_layout = QVBoxLayout()
        left_buttons_groupbox = QGroupBox('User Actions')
        left_buttons_layout.addWidget(left_buttons_groupbox)
        
        buttons_text = deque(['First', 'Second', 'Third', 'Fourth', 'Fifth'])
        for i in range(5):
            button = QPushButton()
            button.setText(buttons_text.popleft())
            # button.setFont(QFont(fonts[0], 12))
            button.setFixedWidth(250)
            button.setFixedHeight(40)
            left_buttons_layout.addWidget(button)

        
        
        """INIT THE MAIN LAYOUT"""
        main_layout = QGridLayout()
        main_layout.addWidget(user_info_groupbox, 0, 0)
        main_layout.addLayout(left_buttons_layout, 1, 0)
        """EXAMINE BELOW TWO LINES HOW EXACTLY THEY APPLY THE LOGIC IN THE UI"""
        main_layout.setRowStretch(4, 2)
        main_layout.setColumnStretch(4, 2)
        self.setLayout(main_layout)
        self.show()
    

app = QApplication(sys.argv)
global login_window
login_window = MainMenu()
login_window.show()
app.exec()

