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

sys.path.append(r'..')
from collections import deque
from db_handle import postgres_conn
import subcategories

# This global variable should be modified to accept it's value dynamically, based on the cattegory button clicked
global subcategory_name
subcategory_name = ''

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(200, 150, 1500, 700)
        self.setMaximumWidth(1500)
        self.setMaximumHeight(700)
        
        """INIT CONNECTION TO THE DATABASE"""
        postgres_conn.admin_client()
        
        def open_func(subcat_name):
            global subcategory_name
            subcategory_name = subcat_name
            open_subcategories()

        functions_dict = {
            'food_open': lambda: open_func("Food"),
            'books_open': lambda: open_func("Books"),
            'drinks_open': lambda: open_func("Drinks"),
            'accessories_open': lambda: open_func("Accessories"),
            'homeandliving_open': lambda: open_func("Home and Living"),
            'hair_open': lambda: open_func("Hair"),
            'sports_open': lambda: open_func("Sports"),
            'beachwear_open': lambda: open_func("Beachwear"),
            'shoes_open': lambda: open_func("Shoes"),
            'electronics_open': lambda: open_func("Electronics"),
            'cosmetics_open': lambda: open_func("Cosmetics"),
            'clothes_open': lambda: open_func("Clothes"),
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
        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT customer_id, first_name, last_name, total_orders FROM customers WHERE username = 'pesho'")
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

        
        buttons_text = deque(['Edit Account', 'View My Orders', 'Payment Options'])
        while buttons_text:
            button = QPushButton()
            button.setText(buttons_text.popleft())
            button.setFont(QFont(fonts[0], 12))
            button.setFixedWidth(250)
            button.setFixedHeight(30)
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
        categories_groupbox = QGroupBox("Categories")

        categories_grid_layout = QGridLayout()

        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT category_name, category_description, category_function, image_url FROM categories ORDER BY category_name ASC;")
        result = postgres_conn.POSTGRES_CURSOR.fetchmany(12)
        categories = deque([x[0] for x in result[0:12]])
        categories_description = deque([x[1] for x in result[0:12]])
        categories_functions = deque([x[2] for x in result[0:12]])

        for row in range(3):
            for col in range(4):
                if categories:
                    current_groupbox = QGroupBox()
                    current_groupbox.setStyleSheet("border: 2px solid red")
                    current_groupbox.setMaximumWidth(300)

                    current_vertical_layout = QVBoxLayout()
                    current_vertical_layout.setAlignment(Qt.AlignBottom)

                    category_name = QLabel(categories.popleft())
                    category_name.setFont(QFont(fonts[0], 9))
                    cat_name_shadow_effect = QGraphicsDropShadowEffect()
                    cat_name_shadow_effect.setBlurRadius(2)
                    cat_name_shadow_effect.setOffset(1, 1)
                    cat_name_shadow_effect.setColor(QColor("blue"))
                    category_name.setGraphicsEffect(cat_name_shadow_effect)
                    category_name.setAlignment(Qt.AlignCenter)
                    category_name.setStyleSheet("background-color: rgba(255, 255, 255, 255);" \
                                                "border-radius: 10px;")

                    image = f"../img/categories/{category_name.text()}.png"
                    groupbox_stylesheet = f"QGroupBox {{ background-image: url({image});" \
                                          f"border-radius: 10px;" \
                                          f"}}"
                    current_groupbox.setStyleSheet(groupbox_stylesheet)

                    category_description = QLabel("background-color: #FFFAFF;")
                    category_description.setText(f"{categories_description.popleft()}")
                    category_description.setFont(QFont(fonts[0], 11))
                    category_description.setStyleSheet("color: rgb(0, 0, 0);")
                    cat_desc_shadow_effect = QGraphicsDropShadowEffect()
                    cat_desc_shadow_effect.setBlurRadius(2)
                    cat_desc_shadow_effect.setOffset(2, 1)
                    cat_desc_shadow_effect.setColor(QColor("white"))
                    category_description.setGraphicsEffect(cat_desc_shadow_effect)

                    category_button = QPushButton()
                    category_button.setText(category_name.text())
                    category_button.setFont(QFont(fonts[0], 11))
                    category_button.setMaximumWidth(150)

                    current_function_name = categories_functions.popleft() + "_open"
                    category_button.clicked.connect(functions_dict[current_function_name])

                    current_vertical_layout.addWidget(category_button)

                    current_groupbox.setLayout(current_vertical_layout)
                    categories_grid_layout.addWidget(current_groupbox, row, col)

        categories_groupbox.setLayout(categories_grid_layout)

        """INIT THE MAIN LAYOUT"""
        main_layout = QGridLayout()
        main_layout.addWidget(user_info_groupbox, 0, 0)
        main_layout.addWidget(left_buttons_groupbox, 1, 0)
        main_layout.addWidget(top_buttons_groupbox, 0, 1)
        main_layout.addWidget(categories_groupbox, 1, 1)

        """EXAMINE BELOW TWO LINES HOW EXACTLY THEY APPLY THE LOGIC IN THE UI"""
        main_layout.setRowStretch(1, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)
        self.show()
        
        def open_subcategories():
            subcategories.start_window(subcategory_name)
            main_window.hide()


def open_app():
    app = QApplication(sys.argv)
    global main_window
    main_window = MainMenu()
    main_window.show()
    app.exec()

def start_window():
    global main_menu_window
    main_menu_window = MainMenu()
    main_menu_window.show()

if __name__ == '__main__':
    open_app()
