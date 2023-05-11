#!/usr/bin/python3

# Import PyQt5 Engine 
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton,
                             QGridLayout,  
                             QLabel,
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
        
        
        """Add custom font to array, ready to be loaded to any text object"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font >= 0:
            fonts = QFontDatabase.applicationFontFamilies(font)
        else:
            print("Error loading fonts!")
        
        
        """Init the main layout"""
        main_layout = QGridLayout()
        
        """Init top left layout"""
        user_info = QVBoxLayout()
        user_name = QLabel()
        user_name.setText("Some User")

        
        user_info.addWidget(user_name)
        
        """Init bottom left layout"""
        buttons_layout = QVBoxLayout()
        """Left Buttons Layout"""
        buttons_text = deque(['First', 'Second', 'Third', 'Fourth', 'Fifth'])
        for i in range(5):
            button = QPushButton()
            button.setText(buttons_text.popleft())
            # button.setFont(QFont(fonts[0]), 12)
            button.setFixedWidth(300)
            button.setFixedHeight(40)
            buttons_layout.addWidget(button)

        
        

    
    
        main_layout.addLayout(user_info, 0, 0)
        main_layout.addLayout(buttons_layout, 1, 0)
        self.setLayout(main_layout)
        self.show()

    

app = QApplication(sys.argv)
global login_window
login_window = MainMenu()
login_window.show()
app.exec()

