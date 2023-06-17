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
# from products import products_menu


# global subcategory_name
subcategory_name = ''


class SubcategoriesMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subcategories Menu")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(200, 150, 1500, 700)
        self.setMaximumWidth(1500)
        self.setMaximumHeight(700)

        """INIT CONNECTION TO THE DATABASE"""
        postgres_conn.admin_client()

        def food_open():
            print("I am eating some food")

        def books_open():
            print("I am reading books")

        def drinks_open():
            print("I am drinking some drinks")



        functions_dict = {
            'food_open': lambda: food_open(),
            'books_open': lambda: books_open(),
            'drinks_open': lambda: drinks_open(),
        }

        """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font < 0:
            print('Error loading fonts!')
        fonts = QFontDatabase.applicationFontFamilies(font)

        """CREATE THE USER INFO VERTICAL LAYOUT"""
        user_info_groupbox = QGroupBox('User Information')
        postgres_conn.POSTGRES_CURSOR.execute("SELECT current_user;")
        current_user = postgres_conn.POSTGRES_CURSOR.fetchone()
        # The query below should be modified once we implement the main_menu window with rest of the application. WHERE username = {current_user}
        postgres_conn.POSTGRES_CURSOR.execute(
            f"SELECT customer_id, first_name, last_name, total_orders FROM customers WHERE username = 'pesho'")
        user_info = postgres_conn.POSTGRES_CURSOR.fetchone()

        user_name = QLabel(f"Hello, {user_info[1]} {user_info[2]}")
        user_name.setFont(QFont(fonts[0], 12))

        user_id = QLabel(f"Your ID is {user_info[0]}")
        user_id.setFont(QFont(fonts[0], 12))
        user_info_layout = QVBoxLayout()

        user_total_orders = QLabel(f"Total orders: {user_info[3]}")
        user_total_orders.setFont(QFont(fonts[0], 12))

        user_info_layout.addWidget(user_name)
        user_info_layout.addWidget(user_id)
        user_info_layout.addWidget(user_total_orders)
        user_info_layout.addStretch(0)
        user_info_layout.addSpacing(100)
        user_info_groupbox.setLayout(user_info_layout)

        """CREATE THE LEFT BUTTONS LAYOUT"""
        left_buttons_groupbox = QGroupBox('User Actions')
        left_buttons_layout = QVBoxLayout()

        buttons_text = deque(['Edit Account', 'View My Orders', 'Payment Options', 'Fourth', 'Fifth'])
        while buttons_text:
            button = QPushButton()
            button.setText(buttons_text.popleft())
            button.setFont(QFont(fonts[0], 12))
            button.setFixedWidth(250)
            button.setFixedHeight(30)
            # button.setStyleSheet("background-color: rgb(51, 153, 255)")
            left_buttons_layout.addWidget(button)

        left_buttons_layout.addStretch(0)
        left_buttons_layout.addSpacing(100)
        left_buttons_groupbox.setLayout(left_buttons_layout)

        """CREATE THE TOP LAYOUT"""
        top_buttons_groupbox = QGroupBox("Top menu")
        top_buttons_layout = QHBoxLayout()

        favourites_button = QPushButton()
        favourites_button.setText("Favourites")
        favourites_button.setFont(QFont(fonts[0], 9))
        favourites_button.setFixedWidth(120)
        favourites_button.setFixedHeight(30)

        about_button = QPushButton()
        about_button.setText("About")
        about_button.setFont(QFont(fonts[0], 9))
        about_button.setFixedWidth(120)
        about_button.setFixedHeight(30)

        log_out_button = QPushButton()
        log_out_button.setText("Log Out")
        log_out_button.setFont(QFont(fonts[0], 9))
        log_out_button.setFixedWidth(100)
        log_out_button.setFixedHeight(30)

        top_buttons_layout.addStretch(0)
        top_buttons_layout.addSpacing(1000)

        top_buttons_layout.addWidget(favourites_button)
        top_buttons_layout.addWidget(about_button)
        top_buttons_layout.addWidget(log_out_button)

        top_buttons_groupbox.setLayout(top_buttons_layout)

        """CREATE THE CATEGORIES LAYOUT"""
        subcategories_groupbox = QGroupBox("Categories")

        image = f"../img/background.png"
        subcats_groupbox_stylesheet = f"QGroupBox {{ background-image: url({image});" \
                                      f"border-radius: 10px;" \
                                      f"}}"
        subcategories_groupbox.setStyleSheet(subcats_groupbox_stylesheet)

        subcategories_grid_layout = QGridLayout()

        global subcategory_name
        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT subcategory_name FROM subcategories where parent_category = '{subcategory_name}' ORDER BY subcategory_name ASC;")
        result = postgres_conn.POSTGRES_CURSOR.fetchall()
        subcategories = deque([x[0] for x in result])
        subcategories_len = len(subcategories)
        # print(subcategories)

        def subcats_func(subcat_name):
            return lambda: open_products(subcat_name)

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
        
        subcategories_groupbox.setLayout(subcategories_grid_layout)

        """INIT THE MAIN LAYOUT"""
        main_layout = QGridLayout()
        main_layout.addWidget(user_info_groupbox, 0, 0)
        main_layout.addWidget(left_buttons_groupbox, 1, 0)
        main_layout.addWidget(top_buttons_groupbox, 0, 1)
        main_layout.addWidget(subcategories_groupbox, 1, 1)

        
        def open_products(cat):
            subcategories_groupbox.hide()
            
            
            products_groupbox = QGroupBox("Products")
            products_grid_layout = QGridLayout()
            
            """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
            font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
            if font < 0:
                print('Error loading fonts!')
            fonts = QFontDatabase.applicationFontFamilies(font)

            postgres_conn.admin_client()

            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT product_name, product_description, product_id FROM products WHERE subcategory = '{cat}' ORDER BY product_name ASC;")

            result = postgres_conn.POSTGRES_CURSOR.fetchall()
            products_names = deque([p[0] for p in result])
            products_descriptions = deque(p[1] for p in result)
            products_ids = deque(p[2] for p in result)
            print(products_names)

            for col in range(3):

                current_vertical_layout = QVBoxLayout()

                product_name = products_names.popleft()

                product_image = QLabel()
                product_image.setFixedSize(325, 220)
                product_image.setPixmap(QPixmap(f"../img/products/{cat}/{product_name}.png"))
                product_image.setScaledContents(True)

                current_title = QLabel()
                current_title.setText('Test Title')
                current_title.setFont(QFont(fonts[0], 12))
                
                current_sku = QLabel()
                current_sku.setText(products_ids.popleft())
                current_sku.setFont(QFont(fonts[0], 12))

                product_description = products_descriptions.popleft()

                current_description = QPlainTextEdit()
                current_description.insertPlainText(product_description)
                current_description.setFont(QFont(fonts[0], 12))
                
                current_buttons_layout = QHBoxLayout()
                current_buttons_layout.setAlignment(Qt.AlignLeft)
                
                current_favorites_button = QPushButton()
                current_favorites_button.setFixedWidth(50)
                current_favorites_button.setFixedHeight(50)
                current_favorites_button.setIcon(QIcon(r'../img/favorite.png'))
                current_favorites_button.setIconSize(QSize(30, 30))
                # current_favorites_button.setText("Add to Favorites")
                current_favorites_button.setFont(QFont(fonts[0], 12))

                current_basket_button = QPushButton()
                # current_basket_button.setText("Add to basket")
                current_basket_button.setFixedWidth(50)
                current_basket_button.setFixedHeight(50)
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
                
                
                
            main_layout.addWidget(products_groupbox, 1, 1)
            # app.quit()

        """EXAMINE BELOW TWO LINES HOW EXACTLY THEY APPLY THE LOGIC IN THE UI"""
        main_layout.setRowStretch(1, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)
        self.show()

   

def start_subcategories():
    app = QApplication(sys.argv)
    global subcategories_window
    subcategories_window = SubcategoriesMenu()
    subcategories_window.show()
    app.exec()

def start_window(sub_cat_name):
    global subcategories_window
    global subcategory_name
    subcategory_name = sub_cat_name
    subcategories_window = SubcategoriesMenu()
    subcategories_window.show()
    