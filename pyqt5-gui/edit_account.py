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

def open_edit_account():
    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)
    
    
    global user_data
    user_data = []
    current_user = postgres_conn.POSTGRES_CURSOR("SELECT current_user")
    # Change to dynamic query in implementation
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT customer_id, username, first_name, last_name, phone, email_address FROM customers WHERE username = 'pesho'")
    result = postgres_conn.POSTGRES_CURSOR.fetchone()

    
    global edit_user_settings_groupbox
    edit_user_settings_groupbox = QGroupBox("Edit Account Settings")
    edit_user_settings_layout = QVBoxLayout()
    edit_user_settings_layout.addStretch()
    edit_user_settings_layout.addSpacing(10)

    text_labels = deque(['ID', 'Username', 'First Name', 'Last Name', 'Phone Number', 'Email Address'])
    text_labels_length = len(text_labels)

    for i in range(text_labels_length):
        current_text_label = QLabel()
        current_text_label.setText(text_labels.popleft())
        current_text_label.setFont(QFont(fonts[0], 12))

        current_line_edit = QLineEdit()
        current_line_edit.setText(str(result[i]))
        current_line_edit.setFont(QFont(fonts[0], 12))
        current_line_edit.setMaximumWidth(250)
        # Disables user_id and username modification
        if i < 2:
            current_line_edit.setReadOnly(True)
        else:
            user_data.append(current_line_edit)

        edit_user_settings_layout.addWidget(current_text_label)
        edit_user_settings_layout.addWidget(current_line_edit)


    edit_user_settings_layout.addStretch()
    edit_user_settings_layout.addSpacing(20)

    reset_button = QPushButton()
    reset_button.setText("Reset to defaults")
    reset_button.setFont(QFont(fonts[0], 12))
    reset_button.setFixedWidth(200)
    reset_button.clicked.connect(lambda: edit_user_settings_groupbox.hide())
    reset_button.clicked.connect(lambda: open_edit_account())

    edit_user_setting_button = QPushButton()
    edit_user_setting_button.setText("Update Info")
    edit_user_setting_button.setFont(QFont(fonts[0], 12))
    edit_user_setting_button.clicked.connect(lambda: edit_user())
    edit_user_setting_button.setFixedWidth(200)

    edit_user_settings_layout.addWidget(reset_button)
    edit_user_settings_layout.addWidget(edit_user_setting_button)

    edit_user_settings_groupbox.setLayout(edit_user_settings_layout)

    return edit_user_settings_groupbox


def edit_user():
    # Make this query dynamically accepting the username in production
    edit_user_query = (f"UPDATE customers SET first_name = %s, last_name = %s, phone = %s, email_address = %s WHERE username = 'pesho'")
    postgres_conn.POSTGRES_CURSOR.execute(edit_user_query, (user_data[0].text(), user_data[1].text(), user_data[2].text(), user_data[3].text()))
    postgres_conn.POSTGRES_CONNECTION.commit()


