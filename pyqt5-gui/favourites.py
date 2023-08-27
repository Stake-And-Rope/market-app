#!/usr/bin/python3

# Import PyQt5 Engine
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QScrollArea,
                             QHBoxLayout,
                             QVBoxLayout)

from PyQt5.QtGui import *
from PyQt5.QtCore import *

import math
import sys
sys.path.append(r'.')
sys.path.append(r'..')
from collections import deque
from db_handle import postgres_conn
import login



def favourites_menu():
    favorites_scroll = QScrollArea()
    favorites_widget = QWidget()
    all_products_layout = QVBoxLayout()
    

    def redirect_to_delete_postgres_func(c_product_name):
        return lambda: delete_from_favourite_products(c_product_name)

    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)
    
    """ADMIN CLIENT TO THE POSTGRE DATABASE"""
    admin_cursor = postgres_conn.POSTGRES_CURSOR
    admin_connection = postgres_conn.POSTGRES_CONNECTION

    
    """USER CLIENT TO THE POSTGRE DATABASE"""
    login.user_cursor.execute("SELECT current_user")
    current_user = login.user_cursor.fetchone()
    current_user = current_user[0].replace("_marketapp", "")
    
    """INNER JOIN QUERY THAT WILL GIVE US EVERY PRODUCT'S DATA"""
    admin_cursor.execute(f"select products.product_id, favourite_products.username, "
                                          f"products.product_name, products.single_price, products.quantity, "
                                          f"products.product_description, products.subcategory "
                                          f"from products inner join favourite_products on "
                                          f"favourite_products.product_id=products.product_id "
                                          f"where favourite_products.username = '{current_user}';")
    result = deque(admin_cursor.fetchall())

    for current_product in result:
        product_id, username, product_name, price, quantity, product_description, subcategory = current_product

        current_horizontal_layout = QHBoxLayout()

        product_image = QLabel()
        product_image.setFixedSize(150, 150)
        product_image.setPixmap(QPixmap(f"../img/products/{subcategory}/{product_name}.png"))
        product_image.setScaledContents(True)

        # current_title = QLabel()
        # current_title.setText('Test Title')
        # current_title.setFont(QFont(fonts[0], 12))

        current_sku = QLabel()
        current_sku.setText(product_id)
        current_sku.setFont(QFont(fonts[0], 10))

        current_description = QLabel(product_description)
        current_description.setWordWrap(True)
        current_description.setFont(QFont(fonts[0], 9))

        current_buttons_layout = QHBoxLayout()
        current_buttons_layout.setAlignment(Qt.AlignLeft)

        current_favorites_button = QPushButton()
        current_favorites_button.setFixedWidth(35)
        current_favorites_button.setFixedHeight(35)
        current_favorites_button.setIcon(QIcon(r'../img/favorite.png'))
        current_favorites_button.setIconSize(QSize(30, 30))
        current_favorites_button.clicked.connect(redirect_to_delete_postgres_func(product_name))

        current_basket_button = QPushButton()
        current_basket_button.setFixedWidth(35)
        current_basket_button.setFixedHeight(35)
        current_basket_button.setIcon(QIcon(r'../img/shoppingcart.png'))
        current_basket_button.setIconSize(QSize(30, 30))

        current_buttons_layout.addWidget(current_favorites_button)
        current_buttons_layout.addWidget(current_basket_button)

        current_horizontal_layout.insertWidget(0, product_image)
        # current_horizontal_layout.addWidget(current_title)
        current_horizontal_layout.addWidget(current_sku)
        current_horizontal_layout.addWidget(current_description)
        current_horizontal_layout.addLayout(current_buttons_layout)

        # current_horizontal_layout.addStretch()
        # current_horizontal_layout.addSpacing(10)

        all_products_layout.addLayout(current_horizontal_layout)
        all_products_layout.addStretch()
        all_products_layout.addSpacing(20)

    favorites_widget.setLayout(all_products_layout)

    favorites_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    favorites_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    favorites_scroll.setWidgetResizable(True)
    favorites_scroll.setWidget(favorites_widget)

    def delete_from_favourite_products(curr_product_name):
        admin_cursor.execute(f"DELETE FROM favourite_products WHERE product_name = '{curr_product_name}' AND username = '{current_user}';")
        admin_connection.commit()
        print('Deleted')

    return favorites_scroll
