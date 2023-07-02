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

def open_payment_options():
    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)
    
    
    # change the query to dinamyc in production
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT payment_name, payment_type, card_number, card_holder, ccv, expire_date FROM payment_options WHERE username = 'pesho'")
    result = postgres_conn.POSTGRES_CURSOR.fetchone()
    text_labels = deque(['Payment Name', 'Payment Type', 'Card Number', 'Card Holder', 'CCV Code', 'Expire Date'])
    text_labels_len = len(text_labels)

    global payment_options_groupbox
    payment_options_groupbox = QGroupBox("Payment Options")

    payment_options_layout = QVBoxLayout()
    payment_options_layout.addStretch()
    payment_options_layout.addSpacing(5)
    for i in range(text_labels_len):
        inner_horizontal_layout = QHBoxLayout()
        inner_horizontal_layout.addStretch()
        inner_horizontal_layout.addSpacing(0)

        current_text_label = QLabel()
        current_text_label.setText(text_labels.popleft())
        current_text_label.setFont(QFont(fonts[0], 12))
        current_text_label.setAlignment(Qt.AlignLeft)

        current_info_label = QLineEdit()
        current_info_label.setText(str(result[i]))
        current_info_label.setFont(QFont(fonts[0], 12))
        current_info_label.setMaximumWidth(250)

        inner_horizontal_layout.addWidget(current_text_label)
        inner_horizontal_layout.addWidget(current_info_label)

        payment_options_layout.addLayout(inner_horizontal_layout)

    payment_options_groupbox.setLayout(payment_options_layout)

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