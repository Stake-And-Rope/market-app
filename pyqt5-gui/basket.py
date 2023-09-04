#!/usr/bin/python3

# Import PyQt5 Engine
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QScrollArea,
                             QHBoxLayout,
                             QVBoxLayout,
                             QSpinBox,
                             )

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import sys
sys.path.append(r'.')
sys.path.append(r'..')
from collections import deque
from db_handle import postgres_conn 
import login

def basket_menu():
    basket_menu_scroll = QScrollArea()
    basket_widget = QWidget()
    basket_menu_h_layout = QVBoxLayout()  # Vertical Layout
    
    """ADMIN CLIENT TO THE POSTGRE DATABASE"""
    admin_cursor = postgres_conn.POSTGRES_CURSOR
    admin_connection = postgres_conn.POSTGRES_CONNECTION

    """USER CLIENT TO THE POSTGRE DATABASE"""
    login.user_cursor.execute("SELECT current_user")
    current_user = login.user_cursor.fetchone()
    current_user = current_user[0].replace("_marketapp", "")
    print(f"From basket print: {current_user}")

    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)

    """INNER JOIN QUERY THAT WILL GIVE US THE PRODUCTS' DESCRIPTIONS AND SUBCATEGORIES"""
    admin_cursor.execute(f"select products.product_id, products.product_name, products.product_description, "
                         f"products.subcategory, products.single_price, basket.quantity, basket.total_value "
                         f"from products inner join basket on basket.product_id=products.product_id "
                         f"where basket.username = '{current_user}';")

    result = deque(admin_cursor.fetchall())

    for current_product in result:
        product_id, product_name, product_description, product_subcategory, single_price, quantity, total_value = current_product

        current_horizontal_layout = QHBoxLayout()  # Horizontal layout for the product

        product_image = QLabel()
        product_image.setFixedSize(150, 150)
        product_image.setPixmap(QPixmap(f"../img/products/{product_subcategory}/{product_name}.png"))
        product_image.setScaledContents(True)

        # current_title = QLabel()
        # current_title.setText("Test Title")
        # current_title.setFont(QFont(fonts[0], 12))

        current_sku = QLabel()
        current_sku.setText(product_id)
        # current_sku.setFont(QFont(fonts[0], 10))
        basket_font = QFont(fonts[0], 10)
        basket_font.setWeight(QFont.Weight.Light + 30)
        current_sku.setFont(basket_font)

        current_description = QLabel(product_description)
        current_description.setWordWrap(True)
        current_description.setFont(QFont(fonts[0], 9))
        basket_font.setPointSize(9)
        current_description.setFont(basket_font)

        current_buttons_layout = QHBoxLayout()
        current_buttons_layout.setAlignment(Qt.AlignLeft)

        current_spin_box = QSpinBox()
        current_spin_box.setValue(int(quantity))

        current_favourites_button = QPushButton()
        current_favourites_button.setFixedWidth(35)
        current_favourites_button.setFixedHeight(35)
        current_favourites_button.setIcon(QIcon(r'../img/favorite.png'))
        current_favourites_button.setIconSize(QSize(30, 30))

        current_basket_button = QPushButton()
        current_basket_button.setFixedWidth(35)
        current_basket_button.setFixedHeight(35)
        current_basket_button.setIcon(QIcon(r'../img/shoppingcart.png'))
        current_basket_button.setIconSize(QSize(30, 30))

        current_buttons_layout.addWidget(current_favourites_button)
        current_buttons_layout.addWidget(current_basket_button)
        current_buttons_layout.addWidget(current_spin_box)

        current_horizontal_layout.insertWidget(0, product_image)
        # current_horizontal_layout.addWidget(current_title)
        current_horizontal_layout.addWidget(current_sku)
        current_horizontal_layout.addWidget(current_description)
        current_horizontal_layout.addLayout(current_buttons_layout)

        basket_menu_h_layout.addLayout(current_horizontal_layout)
        basket_menu_h_layout.addStretch()
        basket_menu_h_layout.addSpacing(20)

    basket_widget.setLayout(basket_menu_h_layout)

    basket_menu_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    basket_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    basket_menu_scroll.setWidgetResizable(True)
    basket_menu_scroll.setWidget(basket_widget)






    # for row in range(rows):
    #     horizontal_products_layout = QHBoxLayout()
    #     for col in range(3):
    #         if result:
    #             current_product = result.popleft()
    #             product_id, product_name, product_description, product_subcategory, single_price, quantity, total_value = current_product
    #
    #             current_vertical_layout = QVBoxLayout()  # Vertical layout for the product
    #
    #             product_image = QLabel()
    #             product_image.setFixedSize(250, 200)
    #             product_image.setPixmap(QPixmap(f"../img/products/{product_subcategory}/{product_name}.png"))
    #             product_image.setScaledContents(True)
    #
    #             current_title = QLabel()
    #             current_title.setText("Test Title")
    #             current_title.setFont(QFont(fonts[0], 12))
    #
    #             current_sku = QLabel()
    #             current_sku.setText(product_id)
    #             current_title.setFont(QFont(fonts[0], 10))
    #
    #             current_description = QLabel(product_description)
    #             current_description.setWordWrap(True)
    #             current_description.setFont(QFont(fonts[0], 9))
    #
    #             current_buttons_layout = QHBoxLayout()
    #             current_buttons_layout.setAlignment(Qt.AlignLeft)
    #
    #             current_spin_box = QSpinBox()
    #             current_spin_box.setValue(int(quantity))
    #
    #             current_favourites_button = QPushButton()
    #             current_favourites_button.setFixedWidth(35)
    #             current_favourites_button.setFixedHeight(35)
    #             current_favourites_button.setIcon(QIcon(r'../img/favorite.png'))
    #             current_favourites_button.setIconSize(QSize(30, 30))
    #
    #             current_basket_button = QPushButton()
    #             current_basket_button.setFixedWidth(35)
    #             current_basket_button.setFixedHeight(35)
    #             current_basket_button.setIcon(QIcon(r'../img/shoppingcart.png'))
    #             current_basket_button.setIconSize(QSize(30, 30))
    #
    #             current_buttons_layout.addWidget(current_favourites_button)
    #             current_buttons_layout.addWidget(current_basket_button)
    #             current_buttons_layout.addWidget(current_spin_box)
    #
    #             current_vertical_layout.insertWidget(0, product_image)
    #             current_vertical_layout.addWidget(current_title)
    #             current_vertical_layout.addWidget(current_sku)
    #             current_vertical_layout.addWidget(current_description)
    #             current_vertical_layout.addLayout(current_buttons_layout)
    #
    #             current_vertical_layout.addStretch()
    #             current_vertical_layout.addSpacing(10)
    #
    #             horizontal_products_layout.addLayout(current_vertical_layout)
    #
    #     basket_menu_h_layout.addLayout(horizontal_products_layout)
    #     basket_widget.setLayout(basket_menu_h_layout)
    #
    # basket_menu_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    # basket_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    # basket_menu_scroll.setWidgetResizable(True)
    # basket_menu_scroll.setWidget(basket_widget)

    return basket_menu_scroll
