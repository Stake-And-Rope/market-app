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
    app = QApplication(sys.argv)
    products_groupbox = QGroupBox("Products")
    products_grid_layout = QGridLayout()

    postgres_conn.admin_client()

    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT product_name FROM products WHERE subcategory = '{subcategory_name}' ORDER BY product_name ASC;")

    result = postgres_conn.POSTGRES_CURSOR.fetchall()
    products_names = deque([p[0] for p in result])
    print(products_names)

    for col in range(3):

        current_vertical_layout = QVBoxLayout()

        product_name = products_names.popleft()

        product_image = QLabel()
        product_image.setFixedSize(325, 220)
        product_image.setPixmap(QPixmap(f"../img/products/Sunglasses/{product_name}.png"))
        product_image.setScaledContents(True)

        current_description = QLabel()
        current_description.setText("Test description")

        current_vertical_layout.insertWidget(0, product_image)
        current_vertical_layout.addWidget(current_description)

        products_grid_layout.addLayout(current_vertical_layout, 0, col)
    
    products_groupbox.setLayout(products_grid_layout)
    return products_groupbox

    # main_layout.setLayout(products_grid_layout, 1, 1)

# products_menu("Accessories", "Sunglasses")
this_groupbox = products_menu('Sunglasses')
