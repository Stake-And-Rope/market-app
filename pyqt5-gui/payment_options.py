#!/usr/bin/python3
"""IMPORT PyQt5 ENGINE"""
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
                             QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect,
                             )

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
sys.path.append(r'..')
from collections import deque
from db_handle import postgres_conn

"""ADMIN CLIENT TO THE POSTGRE DATABASE"""
admin_cursor = postgres_conn.POSTGRES_CURSOR
admin_connection = postgres_conn.POSTGRES_CONNECTION

"""USER CLIENT TO THE POSTGRE DATABASE"""
user_cursor = postgres_conn.USER_POSTGRES_CURSOR
user_connection = postgres_conn.USER_POSTGRES_CONNECTION

def open_payment_options():
    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)
    
    
    # change the query to dinamyc in production
    admin_cursor.execute(f"SELECT * FROM payment_options WHERE username = 'pesho'")
    result = admin_cursor.fetchall()
    len_result = len(result)

    global payment_options_groupbox
    payment_options_groupbox = QGroupBox("Payment Options")
    payment_options_groupbox.setAlignment(Qt.AlignLeft)


    main_payment_layout = QHBoxLayout()
    main_payment_layout.addStretch()
    main_payment_layout.addSpacing(10)
    main_payment_layout.setAlignment(Qt.AlignCenter)
    
    for i in result:
        current_payment_option = QVBoxLayout()
        current_payment_option.setAlignment(Qt.AlignRight)
        text_labels = deque(['Payment Code', 'Payment Name', 'Payment Type', 'Card Number', 'Card Holder', 'CCV', 'Expire Date', 'Default', 'Username'])
        for j in range(len(i)):
            current_line = QHBoxLayout()
            current_line.addStretch()
            current_line.addSpacing(2)
            left_side = QLabel(text_labels.popleft() + ": ")
            left_side.setFont(QFont(fonts[0], 12))
            left_side.setAlignment(Qt.AlignCenter)
            
            right_side = QLabel(str(i[j]))
            right_side.setAlignment(Qt.AlignCenter)
            
            current_line.addWidget(left_side)
            current_line.addWidget(right_side)
            
            current_payment_option.addLayout(current_line)
        main_payment_layout.addLayout(current_payment_option)
            
    payment_options_groupbox.setLayout(main_payment_layout)
    

    return payment_options_groupbox





    # categories_groupbox.hide()
    # main_layout.addWidget(payment_options_groupbox, 1, 1)
    # buttons[-1].setEnabled(False)
    
    # payment_type_layout = QHBoxLayout()
    # payment_type = QLabel()
    # payment_type.setText('Visa Debit')
    # payment_type.setFont(QFont(fonts[0], 12))
    # visa_img = r'../img/visa.png'
    # mastercard_img = r'../img/mastercard.png'
    # revolut_img = r'../img/revolut.png'
    # payment_icon = QLabel()
    # if 'Visa' in payment_type.text():
    #     payment_icon.setPixmap(visa_img)
    # elif 'Mastercard' in payment_type.text():
    #     payment_icon.setPixmap(mastercard_img)
    # elif 'Revolut' in payment_type.text():
    #     payment_icon.setPixmap(revolut_img)
    # payment_icon.setFixedHeight(10)
    # payment_icon.setFixedWidth(10)