#!/usr/bin/python3

# Import PyQt5 Engine
from PyQt5.QtWidgets import (
                             QPushButton,
                             QGridLayout,
                             QLabel,
                             QGroupBox,
                             QVBoxLayout,
                             QGraphicsDropShadowEffect,
                             )

from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
sys.path.append(r'.')
sys.path.append(r'..')
from collections import deque
from db_handle import postgres_conn
import products, login




def open_subcategory(subcatname):
    """ADMIN CLIENT TO THE POSTGRE DATABASE"""
    admin_cursor = postgres_conn.POSTGRES_CURSOR
    admin_connection = postgres_conn.POSTGRES_CONNECTION

    """USER CLIENT TO THE POSTGRE DATABASE"""
    login.user_cursor.execute("SELECT current_user")
    current_user = login.user_cursor.fetchone()
    current_user = current_user[0].replace("_marketapp", "")
    
    global subcategory_name
    global subcategories_groupbox

    """OPEN THE PRODUCTS BASED ON THE SUBCATEGORY CALLED BY THE USER"""
    def subcats_func(subcat_name):
         return lambda: open_products(subcat_name)

    """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
    font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
    if font < 0:
        print('Error loading fonts!')
    fonts = QFontDatabase.applicationFontFamilies(font)

    """CREATE THE SUBCATEGORIES LAYOUT"""
    subcategories_groupbox = QGroupBox()

    image = f"../img/background.png"
    subcats_groupbox_stylesheet = f"QGroupBox {{ background-image: url({image});" \
                                    f"border-radius: 10px;" \
                                    f"}}"
    subcategories_groupbox.setStyleSheet(subcats_groupbox_stylesheet)

    main_grid_layout = QGridLayout()
    subcategories_grid_layout = QGridLayout()
    
    global subcategory_name
    admin_cursor.execute(f"SELECT subcategory_name FROM subcategories where parent_category = '{subcatname}' ORDER BY subcategory_name ASC;")
    result = admin_cursor.fetchall()
    subcategories = deque([x[0] for x in result])

    for row in range(3):
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
        subcategory_button.setProperty("class", "categories_buttons")
        subcategory_button.setMaximumWidth(150)
        if len(subcategory_name.text()) >= 13:
            subcategory_button.setMaximumWidth(205)
            if subcategory_name.text() == "Non-Alcohol Beverages" or subcategory_name.text() == "Photography Gadgets"\
                    or subcategory_name.text() == "Household Appliances":
                subcategory_button.setMaximumWidth(235)
        subcategory_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        subcategory_button.clicked.connect(subcats_func(subcategory_name.text()))


        current_vertical_layout.addWidget(subcategory_button)

        current_groupbox.setLayout(current_vertical_layout)
        subcategories_grid_layout.addWidget(current_groupbox, 0, row)
    main_grid_layout.addLayout(subcategories_grid_layout, 0, 0)
    
    subcategories_groupbox.setLayout(main_grid_layout)
    
    def open_products(cat):
        product_layout = products.products_menu(cat)
        main_grid_layout.addWidget(product_layout, 1, 0)
        subcategories_groupbox.setLayout(main_grid_layout)

    
    return subcategories_groupbox



 


