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
        favourites_button.setFixedHeight(23)

        log_out_button = QPushButton()
        log_out_button.setText("Log Out")
        log_out_button.setFont(QFont(fonts[0], 9))
        log_out_button.setFixedWidth(100)
        log_out_button.setFixedHeight(23)

        top_buttons_layout.addStretch(0)
        top_buttons_layout.addSpacing(1000)

        top_buttons_layout.addWidget(favourites_button)
        top_buttons_layout.addWidget(log_out_button)

        top_buttons_groupbox.setLayout(top_buttons_layout)

        """CREATE THE CATEGORIES LAYOUT"""
        subcategories_groupbox = QGroupBox("Categories")

        subcategories_grid_layout = QGridLayout()

        global subcategory_name
        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT subcategory_name FROM subcategories where parent_category = '{subcategory_name}' ORDER BY subcategory_name ASC;")
        result = postgres_conn.POSTGRES_CURSOR.fetchall()
        subcategories = deque([x[0] for x in result])
        print(subcategories)

        for row in range(3):
            for col in range(4):
                if subcategories:
                    current_groupbox = QGroupBox()
                    # current_groupbox.setStyleSheet("border: 2px solid red")
                    current_groupbox.setMaximumWidth(300)

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

                    # IMPORTANTE !!!!!!!!
                    # image = f"../img/categories/{category_name.text()}.png"
                    # groupbox_stylesheet = f"QGroupBox {{ background-image: url({image});" \
                    #                       f"border-radius: 10px;" \
                    #                       f"}}"
                    # current_groupbox.setStyleSheet(groupbox_stylesheet)

                    subcategory_button = QPushButton()
                    subcategory_button.setText(subcategory_name.text())
                    subcategory_button.setFont(QFont(fonts[0], 11))
                    subcategory_button.setMaximumWidth(150)
                    subcategory_button.setStyleSheet("background-color: rgba(255, 255, 0)")

                    # current_function_name = categories_functions.popleft()
                    # print(current_function_name)
                    # category_button.clicked.connect(functions_dict[current_function_name])

                    current_vertical_layout.addWidget(subcategory_button)

                    current_groupbox.setLayout(current_vertical_layout)
                    subcategories_grid_layout.addWidget(current_groupbox, row, col)

        subcategories_groupbox.setLayout(subcategories_grid_layout)

        """INIT THE MAIN LAYOUT"""
        main_layout = QGridLayout()
        main_layout.addWidget(user_info_groupbox, 0, 0)
        main_layout.addWidget(left_buttons_groupbox, 1, 0)
        main_layout.addWidget(top_buttons_groupbox, 0, 1)
        main_layout.addWidget(subcategories_groupbox, 1, 1)

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
    