#!/usr/bin/python3
import sys
import requests
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
                             QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect,
                             )

from PyQt5.QtGui import *
from PyQt5.QtCore import *

sys.path.append(r'.')
sys.path.append(r'..')
from collections import deque
from db_handle import postgres_conn


def products_menu(subcategory_name):
    global products_groupbox
    
    products_groupbox = QGroupBox("Products")
    products_grid_layout = QGridLayout()
    
    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)

    postgres_conn.admin_client()

    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT product_name, product_description, product_id FROM products WHERE subcategory = '{subcategory_name}' ORDER BY product_name ASC;")

    result = postgres_conn.POSTGRES_CURSOR.fetchall()
    products_names = deque([p[0] for p in result])
    products_descriptions = deque(p[1] for p in result)
    products_ids = deque(p[2] for p in result)
    print(products_names)

    for col in range(3):

        current_vertical_layout = QVBoxLayout()

        product_name = products_names.popleft()

        product_image = QLabel()
        product_image.setFixedSize(250, 200)
        product_image.setPixmap(QPixmap(f"../img/products/{subcategory_name}/{product_name}.png"))
        product_image.setScaledContents(True)

        current_title = QLabel()
        current_title.setText('Test Title')
        current_title.setFont(QFont(fonts[0], 12))
        
        current_sku = QLabel()
        current_sku.setText(products_ids.popleft())
        current_sku.setFont(QFont(fonts[0], 10))

        product_description = products_descriptions.popleft()

        # current_description = QPlainTextEdit()
        # current_description.insertPlainText(product_description)
        # current_description.setFont(QFont(fonts[0], 12))

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
        current_favorites_button.setFont(QFont(fonts[0], 12))

        current_basket_button = QPushButton()
        current_basket_button.setFixedWidth(35)
        current_basket_button.setFixedHeight(35)
        current_basket_button.setIcon(QIcon(r'../img/shoppingcart.png'))
        current_basket_button.setIconSize(QSize(30, 30))
        current_basket_button.setFont(QFont(fonts[0], 12))

        current_buttons_layout.addWidget(current_favorites_button)
        current_buttons_layout.addWidget(current_basket_button)

        current_vertical_layout.insertWidget(0, product_image)
        current_vertical_layout.addWidget(current_title)
        current_vertical_layout.addWidget(current_sku)
        current_vertical_layout.addWidget(current_description)
        current_vertical_layout.addLayout(current_buttons_layout)

        current_vertical_layout.addStretch()
        current_vertical_layout.addSpacing(10)

        products_grid_layout.addLayout(current_vertical_layout, 0, col)

        products_groupbox.setLayout(products_grid_layout)
        
    return products_groupbox
