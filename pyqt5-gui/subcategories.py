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
# from main_menu_dev import subcategory_name
import products, main_menu


global subcategory_name
subcategory_name = ''

def open_subcategory(subcatname):
    """INIT CONNECTION TO THE DATABASE"""
    postgres_conn.admin_client()


    
    
    """OPEN THE PRODUCTS BASED ON THE SUBCATEGORY CALLED BY THE USER"""
    def subcats_func(subcat_name):
         return lambda: open_products(subcat_name)

    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)

    """CREATE THE SUBCATEGORIES LAYOUT"""
    subcategories_groupbox = QGroupBox("SubCategories")

    image = f"../img/background.png"
    subcats_groupbox_stylesheet = f"QGroupBox {{ background-image: url({image});" \
                                    f"border-radius: 10px;" \
                                    f"}}"
    subcategories_groupbox.setStyleSheet(subcats_groupbox_stylesheet)

    main_grid_layout = QGridLayout()
    subcategories_grid_layout = QGridLayout()
    

    global subcategory_name
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT subcategory_name FROM subcategories where parent_category = '{subcatname}' ORDER BY subcategory_name ASC;")
    result = postgres_conn.POSTGRES_CURSOR.fetchall()
    subcategories = deque([x[0] for x in result])

    for row in range(3):
        # for col in range(4):
        # if subcategories:
        current_groupbox = QGroupBox()
        current_groupbox.setMaximumWidth(400)
        current_groupbox.setMaximumHeight(150)

        current_vertical_layout = QVBoxLayout()

        subcategory_name = QLabel(f"{subcategories.popleft()}")
        subcategory_name.setFont(QFont(fonts[0], 9))
        subcat_name_shadow_effect = QGraphicsDropShadowEffect()
        subcat_name_shadow_effect.setBlurRadius(2)
        subcat_name_shadow_effect.setOffset(1, 1)
        subcat_name_shadow_effect.setColor(QColor("blue"))
        subcategory_name.setGraphicsEffect(subcat_name_shadow_effect)
        subcategory_name.setAlignment(Qt.AlignCenter)
        subcategory_name.setStyleSheet("background-color: rgba(255, 255, 255, 255);"
                                    "border-radius: 10px;")

        image = f"../img/subcategories/{subcategory_name.text()}.png"
        groupbox_stylesheet = f"QGroupBox {{ background-image: url({image});" \
                                f"border-radius: 10px;" \
                                f"}}"
        current_groupbox.setStyleSheet(groupbox_stylesheet)

        subcategory_button = QPushButton()
        subcategory_button.setText(subcategory_name.text())
        subcategory_button.setFont(QFont(fonts[0], 11))
        subcategory_button.setMaximumWidth(150)
        subcategory_button.clicked.connect(subcats_func(subcategory_name.text()))


        current_vertical_layout.addWidget(subcategory_button)

        current_groupbox.setLayout(current_vertical_layout)
        subcategories_grid_layout.addWidget(current_groupbox, 0, row)
    main_grid_layout.addLayout(subcategories_grid_layout, 0, 0)
    
    subcategories_groupbox.setLayout(main_grid_layout)
    
    def open_products(cat):
        # subcategories_groupbox.hide()
        product_layout = products.products_menu(cat)
        main_grid_layout.addWidget(product_layout, 1, 0)
        subcategories_groupbox.setLayout(main_grid_layout)
        print(5)
    
    return subcategories_groupbox



 


