#!/usr/bin/python3
"""IMPORT PyQt5 ENGINE"""
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QLineEdit,
                             QDateEdit,
                             QComboBox,
                             QGroupBox,
                             QMessageBox,
                             QPlainTextEdit,
                             QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
sys.path.append(r'..')
from db_handle import postgres_conn
import login

"""ADMIN CLIENT TO THE POSTGRE DATABASE"""
admin_cursor = postgres_conn.POSTGRES_CURSOR
admin_connection = postgres_conn.POSTGRES_CONNECTION

"""USER CLIENT TO THE POSTGRE DATABASE"""
user_cursor = postgres_conn.USER_POSTGRES_CURSOR
user_connection = postgres_conn.USER_POSTGRES_CONNECTION

def open_payment_options():
    login.user_cursor.execute("SELECT current_user")
    global current_user
    current_user = login.user_cursor.fetchone()
    current_user = current_user[0].replace("_marketapp", "")
    
    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)
    
    admin_cursor.execute(f"SELECT * FROM payment_options WHERE username = '{current_user}'")
    result = admin_cursor.fetchall()

    global payment_options_groupbox
    payment_options_groupbox = QGroupBox()
    payment_options_layout = QVBoxLayout()
    payment_options_layout.addStretch()
    payment_options_layout.addSpacing(5)
    payment_options_groupbox.setAlignment(Qt.AlignLeft)
    
    """GENERATE THE USER'S CARD DETAILS AND DRAW THE OBJECTS"""
    for i in range(len(result)):
        current_payment_option = QHBoxLayout()
        current_payment_option.setAlignment(Qt.AlignLeft)
        
        card_type = result[i][2]
        
        payment_type_label = QLabel()
        if card_type == "Visa":
            payment_type_label.setProperty("class", "payment_label_visa")
        elif card_type == "MasterCard":
            payment_type_label.setProperty("class", "payment_label_mastercard")
        elif card_type == "Revolut":
            payment_type_label.setProperty("class", "payment_label_revolut")
        payment_type_label.setFixedSize(64, 64)
        
        payment_name = QLabel()
        payment_name.setText(f'Alias: {result[i][1]} /')
        payment_name.setFont(QFont(fonts[0], 12))
        
        card_holder = QLabel()
        card_holder.setText(f'Card Holder: {result[i][4]} /')
        card_holder.setFont(QFont(fonts[0], 12))
        
        card_number = QLabel()
        card_number.setText(f'Card Number: {result[i][3]} /')
        card_number.setFont(QFont(fonts[0], 12))
        
        date_label = QLabel()
        date_label.setText(f'Valid until: {str(result[i][6])}')
        
        delete_button = QPushButton()
        delete_button.setIcon(QIcon(r"../img/trash.png"))
        delete_button.setIconSize(QSize(32, 32))
        delete_button.setToolTip("Delete Card")
        delete_button.clicked.connect(lambda: open_delete_card())
        
        current_payment_option.addWidget(payment_type_label)
        current_payment_option.addWidget(payment_name)
        current_payment_option.addWidget(card_holder)
        current_payment_option.addWidget(card_number)
        current_payment_option.addWidget(date_label)
        current_payment_option.addWidget(delete_button)

        payment_options_layout.addLayout(current_payment_option)
    
    """CREATE NEW CARD - IT WILL POP-OUT NEW WINDOW"""
    add_new_card = QPushButton()
    add_new_card.setText("Add New Card")
    add_new_card.setFont(QFont(fonts[0], 12))
    add_new_card.setFixedSize(150, 30)
    add_new_card.clicked.connect(lambda: open_create_new_card())
    
    payment_options_layout.addWidget(add_new_card)
    
    payment_options_groupbox.setLayout(payment_options_layout)
    
    """DELETE CARD POP-OUT WINDOW IN A SEPARATE CLASS"""
    class DeleteCard(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Delete Card")
            self.setGeometry(650, 300, 300, 200)
            self.setWindowIcon(QIcon(r'../img/market.png'))
            
            delete_card_main_layout = QVBoxLayout()
            
            delete_text = QLabel()
            delete_text.setText("Are you sure you want to delete this card?")
            delete_text.setFont(QFont(fonts[0], 12))
            
            confirm_delete_button = QPushButton()
            confirm_delete_button.setText("Delete Card")
            confirm_delete_button.clicked.connect(lambda: delete_card())
            
            cancel_delete_button = QPushButton()
            cancel_delete_button.setText("Cancel")
            cancel_delete_button.clicked.connect(lambda: cancel_delete())
            
            delete_card_main_layout.addWidget(delete_text)
            delete_card_main_layout.addWidget(confirm_delete_button)
            delete_card_main_layout.addWidget(cancel_delete_button)
            
            def delete_card():
                print()
            
            def cancel_delete():
                delete_card_window.hide()
            
            self.setLayout(delete_card_main_layout)

    """CREATE NEW CARD POP-OUT WINDOW IN A SEPARATE CLASS"""
    class CreateCard(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Create New Payment Card")
            self.setGeometry(650, 300, 300, 200)
            self.setWindowIcon(QIcon(r'../img/market.png'))        
        
            create_card_main_layout = QVBoxLayout()
            create_card_main_layout.addStretch()
            create_card_main_layout.addSpacing(5)

            payment_name_field = QLineEdit()
            payment_name_field.setText("Card Alias")
            payment_name_field.setFont(QFont(fonts[0], 12))
            
            payment_type_field = QComboBox()
            visa_icon = QIcon(r"../img/visa64.png")
            mastercard_icon = QIcon(r"../img/mastercard64.png")
            revolut_icon = QIcon(r"../img/revolut64.png")
            payment_type_field.addItem(visa_icon, "Visa")
            payment_type_field.addItem(mastercard_icon, "Mastercard")
            payment_type_field.addItem(revolut_icon, "Revolut")
            
            card_number_field = QLineEdit()
            card_number_field.setText("Card Number")
            card_number_field.setFont(QFont(fonts[0], 12))
            card_number_field.setMaxLength(14)
            
            card_holder_field = QLineEdit()
            card_holder_field.setText("Cardholder Name")
            card_holder_field.setFont(QFont(fonts[0], 12))
            
            ccv_field = QLineEdit()
            ccv_field.setText("CCV Number")
            ccv_field.setFont(QFont(fonts[0], 12))
            ccv_field.setMaxLength(3)
            
            date_field = QDateEdit(calendarPopup=True)
            date_field.setDateTime(QDateTime.currentDateTime())
            date_field.setFont(QFont(fonts[0], 12))
            
            buttons_layout = QHBoxLayout()
            buttons_layout.addStretch()
            buttons_layout.addSpacing(5)
            
            confirm_create_button = QPushButton()
            confirm_create_button.setText("Save Card")
            confirm_create_button.setFont(QFont(fonts[0], 12))
            
            cancel_create_button = QPushButton()
            cancel_create_button.setText("Cancel")
            cancel_create_button.setFont(QFont(fonts[0], 12))
            cancel_create_button.clicked.connect(lambda: cancel_create())
            
            buttons_layout.addWidget(confirm_create_button)
            buttons_layout.addWidget(cancel_create_button)
            
            create_card_main_layout.addWidget(payment_name_field)
            create_card_main_layout.addWidget(payment_type_field)
            create_card_main_layout.addWidget(card_number_field)
            create_card_main_layout.addWidget(card_holder_field)
            create_card_main_layout.addWidget(ccv_field)
            create_card_main_layout.addWidget(date_field)
            create_card_main_layout.addLayout(buttons_layout)

            self.setLayout(create_card_main_layout)
            
            def create_card():
                pass
            
            def cancel_create():
                create_card_window.hide()

    
    def open_create_new_card():
        global create_card_window
        create_card_window = CreateCard()
        create_card_window.show()


    def open_delete_card():
        global delete_card_window
        delete_card_window = DeleteCard()
        delete_card_window.show()
            
    

    return payment_options_groupbox



