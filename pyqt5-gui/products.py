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


def products_menu(category_name, subcategory_name):
    products_groupbox = QGroupBox("Products")
    products_grid_layout = QGridLayout()

    postgres_conn.admin_client()

    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT product_name FROM products where category = '{category_name}' and subcategory = '{subcategory_name}' ORDER BY product_name ASC;")

    result = postgres_conn.POSTGRES_CURSOR.fetchall()
    products_names = deque([p[0] for p in result])
    print(products_names)

    for col in range(3):
        current_groupbox = QGroupBox()
        current_groupbox.setMaximumWidth(400)
        current_groupbox.setMaximumHeight(500)

        current_vertical_layout = QVBoxLayout()

        product_name = products_names.popleft()

        product_image = QLabel()
        product_image.setPixmap(QPixmap("../img/products/Sunglasses/Sunglasses1.png"))
        product_image.setScaledContents(True)

        current_vertical_layout.addWidget(product_image)
        current_groupbox.setLayout(current_vertical_layout)

        products_grid_layout.addWidget(current_groupbox, 0, col)

    products_groupbox.setLayout(products_grid_layout)

products_menu("Accessories", "Sunglasses")