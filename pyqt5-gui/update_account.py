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


def open_update_account():
        
            """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
            font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
            if font < 0:
                print('Error loading fonts!')
            fonts = QFontDatabase.applicationFontFamilies(font)
            
            
            global user_data
            user_data = []
            # Change to dynamic query in implementation
            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT customer_id, username, first_name, last_name, phone, email_address FROM customers WHERE username = 'pesho'")
            result = postgres_conn.POSTGRES_CURSOR.fetchone()

            update_user_settings_groupbox = QGroupBox("Update Account Settings")
            update_user_settings_layout = QVBoxLayout()
            update_user_settings_layout.addStretch()
            update_user_settings_layout.addSpacing(10)

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

                update_user_settings_layout.addWidget(current_text_label)
                update_user_settings_layout.addWidget(current_line_edit)


            update_user_settings_layout.addStretch()
            update_user_settings_layout.addSpacing(20)

            reset_button = QPushButton()
            reset_button.setText("Reset to defaults")
            reset_button.setFont(QFont(fonts[0], 12))
            reset_button.setFixedWidth(200)
            reset_button.clicked.connect(lambda: update_user_settings_groupbox.hide())
            reset_button.clicked.connect(lambda: open_update_account())

            update_user_setting_button = QPushButton()
            update_user_setting_button.setText("Update Info")
            update_user_setting_button.setFont(QFont(fonts[0], 12))
            update_user_setting_button.clicked.connect(lambda: update_user())
            update_user_setting_button.setFixedWidth(200)

            update_user_settings_layout.addWidget(reset_button)
            update_user_settings_layout.addWidget(update_user_setting_button)

            update_user_settings_groupbox.setLayout(update_user_settings_layout)

            categories_groupbox.hide()
            main_layout.addWidget(update_user_settings_groupbox, 1, 1)
            # Disable the button to avoid calling again the function
                # Not the best approach, but for now it will do
            buttons[-1].setEnabled(False)

            global hide_user_update_settings
            def hide_user_update_settings():
                update_user_settings_groupbox.hide()
                categories_groupbox.show()
                # Activate back the button
                buttons[-1].setEnabled(True)


def update_user():
    # Make this query dynamically accepting the username in production
    update_user_query = (f"UPDATE customers SET first_name = %s, last_name = %s, phone = %s, email_address = %s WHERE username = 'pesho'")
    postgres_conn.POSTGRES_CURSOR.execute(update_user_query, (user_data[0].text(), user_data[1].text(), user_data[2].text(), user_data[3].text()))
    postgres_conn.POSTGRES_CONNECTION.commit()
