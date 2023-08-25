#!/usr/bin/python3

# Import PyQt5 Engine
from PyQt5.QtWidgets import (
                             QPushButton,
                             QGridLayout,
                             QLabel,
                             QGroupBox,
                             QMessageBox,
                             QHBoxLayout,
                             QVBoxLayout,
                             QSpinBox)

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
sys.path.append(r'.')
sys.path.append(r'..')

from collections import deque
from db_handle import postgres_conn
import login


def products_menu(subcategory_name):
    """ADMIN CLIENT TO THE POSTGRE DATABASE"""
    admin_cursor = postgres_conn.POSTGRES_CURSOR
    admin_connection = postgres_conn.POSTGRES_CONNECTION

    """USER CLIENT TO THE POSTGRE DATABASE"""
    login.user_cursor.execute("SELECT current_user")
    current_user = login.user_cursor.fetchone()
    current_user = current_user[0].replace("_marketapp", "")
    
    global products_groupbox
    
    """THIS FUNCTION WILL REDIRECT THE CURRENT PROD ID AND PROD NAME TO THE INSERT TO THE POSTGRE DB FUNCTION"""
    def redirect_to_insert_to_postgre_func(prod_id, prod_name, spin_box):
        return lambda: insert_into_favourite_products(prod_id, prod_name, spin_box)
    
    def redirect_to_insert_to_basket_func(prod_id, prod_name, spin_box, price_for_one):
        return lambda : insert_into_basket(prod_id, prod_name, spin_box, price_for_one)
    
    products_groupbox = QGroupBox()
    products_grid_layout = QGridLayout()

    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)

    admin_cursor.execute(f"SELECT product_name, product_description, product_id, single_price FROM products WHERE subcategory = '{subcategory_name}' ORDER BY product_name ASC;")

    result = postgres_conn.POSTGRES_CURSOR.fetchall()
    products_names = deque([p[0] for p in result])
    products_descriptions = deque(p[1] for p in result)
    products_ids = deque(p[2] for p in result)
    single_prices = deque(p[3] for p in result)

    for col in range(3):

        current_vertical_layout = QVBoxLayout()

        product_name = products_names.popleft()
        product_id = products_ids.popleft()
        single_price = single_prices.popleft()

        product_image = QLabel()
        product_image.setFixedSize(250, 200)
        product_image.setPixmap(QPixmap(f"../img/products/{subcategory_name}/{product_name}.png"))
        product_image.setScaledContents(True)

        current_title = QLabel()
        current_title.setText('Test Title')
        current_title.setFont(QFont(fonts[0], 12))

        current_sku = QLabel()
        current_sku.setText(product_id)
        current_sku.setFont(QFont(fonts[0], 10))

        product_description = products_descriptions.popleft()

        current_description = QLabel(product_description)
        current_description.setWordWrap(True)
        current_description.setFont(QFont(fonts[0], 9))

        current_buttons_layout = QHBoxLayout()
        current_buttons_layout.setAlignment(Qt.AlignLeft)

        current_spin_box = QSpinBox()
        # current_spin_box.setBaseSize(40, 30)  # this doesn't work

        current_favorites_button = QPushButton()
        current_favorites_button.setFixedWidth(35)
        current_favorites_button.setFixedHeight(35)
        current_favorites_button.setIcon(QIcon(r'../img/favorite.png'))
        current_favorites_button.setIconSize(QSize(30, 30))
        current_favorites_button.setFont(QFont(fonts[0], 12))
        current_favorites_button.clicked.connect(redirect_to_insert_to_postgre_func(product_id, product_name, current_spin_box))

        current_basket_button = QPushButton()
        current_basket_button.setFixedWidth(35)
        current_basket_button.setFixedHeight(35)
        current_basket_button.setIcon(QIcon(r'../img/shoppingcart.png'))
        current_basket_button.setIconSize(QSize(30, 30))
        current_basket_button.setFont(QFont(fonts[0], 12))
        current_basket_button.clicked.connect(redirect_to_insert_to_basket_func(product_id, product_name, current_spin_box, single_price))

        current_buttons_layout.addWidget(current_favorites_button)
        current_buttons_layout.addWidget(current_basket_button)
        current_buttons_layout.addWidget(current_spin_box)

        current_vertical_layout.insertWidget(0, product_image)
        current_vertical_layout.addWidget(current_title)
        current_vertical_layout.addWidget(current_sku)
        current_vertical_layout.addWidget(current_description)
        current_vertical_layout.addLayout(current_buttons_layout)

        current_vertical_layout.addStretch()
        current_vertical_layout.addSpacing(10)

        products_grid_layout.addLayout(current_vertical_layout, 0, col)

        products_groupbox.setLayout(products_grid_layout)

        def insert_into_favourite_products(curr_id, curr_product_name, curr_spin_box):
            admin_cursor.execute(f"SELECT * FROM favourite_products WHERE product_id = '{curr_id}' AND username = '{current_user}'")
            result = admin_cursor.fetchall()

            """HERE WE SELECT THE AVAILABLE QUANTITY OF THE PRODUCT AND SEE IF WE CAN ADD IT TO FAVOURITES"""
            admin_cursor.execute(f"SELECT quantity FROM products WHERE product_id='{curr_id}';")
            available_quantity = admin_cursor.fetchone()

            if result:
                error_message_box("Product already exists in favorites.")
            else:
                admin_cursor.execute(f"INSERT INTO favourite_products VALUES ('{current_user}', '{curr_id}', '{curr_product_name}')")
                admin_connection.commit()
        
        def insert_into_basket(curr_id, curr_product_name, curr_spin_box, curr_single_price):
            admin_cursor.execute(f"SELECT * FROM basket WHERE product_id = '{curr_id}' AND username = '{current_user}'")
            result = admin_cursor.fetchall()
            """HERE WE SELECT THE AVAILABLE QUANTITY OF THE PRODUCT AND SEE IF WE CAN ADD IT TO BASKET"""
            admin_cursor.execute(f"SELECT quantity FROM products WHERE product_id='{curr_id}';")
            available_quantity = admin_cursor.fetchone()
            if result:
                error_message_box(f"Product already exists in basket.")  # need to add two options --> "Add more" and "Cancel"
            elif int(str(curr_spin_box.value())) > int(available_quantity[0]):
                error_message_box("You have exceeded the available quantity of this product. "
                                  "Please choose a smaller quantity!")
            else:
                admin_cursor.execute(f"INSERT INTO basket VALUES "
                                                      f"('{current_user}', '{curr_id}', '{curr_product_name}', "
                                                      f"'{curr_spin_box.value()}', '{curr_single_price}')")
                admin_connection.commit()
                print("Added to basket")

        def error_message_box(message):
            error_msg_box = QMessageBox()
            error_msg_box.setIcon(QMessageBox.Warning)
            error_msg_box.setText(message)
            error_msg_box.setWindowTitle("Info Message")
            error_msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box = error_msg_box.exec()

            return msg_box

    return products_groupbox
