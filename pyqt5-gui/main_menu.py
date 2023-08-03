#!/usr/bin/python3
import sys
import requests
"""IMPORT PyQt5 ENGINE"""
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
import about, subcategories, edit_account, payment_options, products, favourites

# This global variable should be modified to accept it's value dynamically, based on the cattegory button clicked
global subcategory_name
subcategory_name = ''
layouts_list = []

"""INIT CONNECTION TO THE DATABASE"""
# postgres_conn.admin_client()

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.setWindowIcon(QIcon(r'../img/market.png'))
        self.setGeometry(200, 150, 1500, 700)
        self.setMaximumWidth(1500)
        self.setMaximumHeight(700)


    
        """OPEN THE PROPER SUBCATEGORY"""
        def open_func(curr_subcat_name):
            global subcategory_name
            subcategory_name = curr_subcat_name
            open_subcategories(subcategory_name)

        def open_category_func(subcat_name):
            return lambda: open_func(subcat_name)

        def open_favourites_func():
            return lambda: open_favourites()

        """LEFT LAYOUT BUTTONS CALL FUNCTION"""
        left_layout_buttons_dict = {
            'edit_account': lambda: open_update_account(),
            'view_my_orders': lambda: open_user_orders(),
            'payment_options': lambda: open_payment_options(),
            'back': lambda: open_categories(),
        }

        """TOP LAYOUT BUTTONS CALL FUNCTIONS"""
        top_layout_buttons_dict = {
            'Favourites': open_favourites_func(),
            'About': lambda: open_about(),
            # TODO: need to add the log out button function
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

        buttons_text = deque(['Edit Account', 'View My Orders', 'Payment Options', 'Back'])
        buttons = deque([])
        while buttons_text:
            button = QPushButton()
            button_text = buttons_text.popleft()
            button.setText(button_text)
            button_function = button_text.replace(" ", "_")
            button_function = button_function.lower()
            button.setFont(QFont(fonts[0], 12))
            button.setFixedWidth(250)
            button.setFixedHeight(30)
            button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            button.clicked.connect(left_layout_buttons_dict[button_function])
            buttons.appendleft(button)

            left_buttons_layout.addWidget(button)

        left_buttons_layout.addStretch(0)
        left_buttons_layout.addSpacing(100)
        left_buttons_groupbox.setLayout(left_buttons_layout)

        """CREATE THE TOP LAYOUT"""
        top_buttons_groupbox = QGroupBox("Top menu")
        top_buttons_layout = QHBoxLayout()

        top_buttons_layout.addStretch(0)
        top_buttons_layout.addSpacing(1000)

        top_buttons_text = deque(['Favourites', 'About'])  # TODO: need to add the 'Log Out' button

        while top_buttons_text:
            curr_top_button = top_buttons_text.popleft()
            top_button = QPushButton()
            top_button.setText(curr_top_button)
            top_button.setFont(QFont(fonts[0], 9))
            top_button.setFixedWidth(120)
            top_button.setFixedHeight(30)
            top_button.setCursor(QCursor(QCursor(Qt.CursorShape.PointingHandCursor)))
            top_button.clicked.connect(top_layout_buttons_dict[curr_top_button])

            top_buttons_layout.addWidget(top_button)

        top_buttons_groupbox.setLayout(top_buttons_layout)

        """CREATE THE CATEGORIES LAYOUT"""
        categories_groupbox = QGroupBox("Categories")

        categories_grid_layout = QGridLayout()

        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT category_name, category_description, category_function, image_url FROM categories ORDER BY category_name ASC;")
        result = postgres_conn.POSTGRES_CURSOR.fetchmany(12)
        categories = deque([x[0] for x in result[0:12]])
        categories_description = deque([x[1] for x in result[0:12]])

        for row in range(3):
            for col in range(4):
                if categories:
                    current_groupbox = QGroupBox()
                    current_groupbox.setStyleSheet("border: 2px solid red")
                    current_groupbox.setMaximumWidth(300)

                    current_vertical_layout = QVBoxLayout()
                    current_vertical_layout.setAlignment(Qt.AlignBottom)

                    category_name = categories.popleft()

                    image = f"../img/categories/{category_name}.png"
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
                    category_button.setText(category_name)
                    category_button.setFont(QFont(fonts[0], 11))
                    category_button.setMaximumWidth(150)
                    category_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

                    category_button.clicked.connect(open_category_func(category_name))

                    current_vertical_layout.addWidget(category_button)

                    current_groupbox.setLayout(current_vertical_layout)
                    categories_grid_layout.addWidget(current_groupbox, row, col)

        categories_groupbox.setLayout(categories_grid_layout)

        """INIT THE MAIN LAYOUT"""
        global main_layout
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

        
        """OPEN EDIT ACCOUNT LAYOUT/REPLACE CATEGORIES LAYOUT"""
        def open_update_account():
            global edit_account_layout
            global layouts_list
            edit_account_layout = edit_account.open_edit_account()
            layouts_list.append(edit_account_layout)
            categories_groupbox.hide()
            try:
                payment_options_layout.hide()
                subcategories_layout.hide()
            except Exception as error:
                print("Payment Options Not Opened")                
            main_layout.addWidget(edit_account_layout, 1, 1)
            # Disable the button to avoid calling again the function
                # Not the best approach, but for now it will do
            buttons[-1].setEnabled(False)
            buttons[-2].setEnabled(True)
            buttons[-3].setEnabled(True)
            buttons[-4].setEnabled(True)
        open_update_account()

        """OPEN PAYMENT OPTIONS LAYOUT/REPLACE CATEGORIES LAYOUT"""
        def open_payment_options():
            global payment_options_layout
            global layouts_list
            payment_options_layout = payment_options.open_payment_options()
            layouts_list.append(payment_options_layout)
            categories_groupbox.hide()
            try:
                edit_account_layout.hide()
                subcategories_layout.hide()
            except Exception as error:
                print("Edit Account Not Opened")            
            main_layout.addWidget(payment_options_layout, 1, 1)
            buttons[-3].setEnabled(False)
            buttons[-1].setEnabled(True)
            buttons[-2].setEnabled(True)
            buttons[-4].setEnabled(True)
        open_payment_options()
        
        """OPEN USER ORDERS HISTORY/REPLACE CATEGORIES LAYOUT"""
        def open_user_orders():
            pass
        
        """OPEN ABOUT WINDOW"""
        def open_about():
            about.start_window()
        
        """OPEN SUBCATEGORIES WINDOW"""
        def open_subcategories(sub_cat_name):
            global subcategories_layout
            global layouts_list
            subcategories_layout = subcategories.open_subcategory(sub_cat_name)
            layouts_list.append(subcategories_layout)
            categories_groupbox.hide()
            main_layout.addWidget(subcategories_layout, 1, 1)

        def open_favourites():
            global favourites_layout
            global layouts_list
            favourites_layout = favourites.favourites_menu()
            layouts_list.append(favourites_layout)
            categories_groupbox.hide()
            main_layout.addWidget(favourites_layout, 1, 1)
        
        
        
        """BRING BACK THE CATEGORIES"""
        def open_categories():
            # Not the best approach, that could be improved
            for i in layouts_list:
                try:
                    i.hide()
                except Exception as error:
                    print(f"{i} is not opened")
            categories_groupbox.show()
            buttons[-1].setEnabled(True)
            buttons[-2].setEnabled(True)
            buttons[-3].setEnabled(True)
            buttons[-4].setEnabled(True)
        open_categories()
        
        
"""OBSOLETE - KEEP FOR NOW FOR DEBUGING PURPOSES, BUT MOST PROBEBLY WONT BE NEEDED"""
def open_app():
    app = QApplication(sys.argv)
    global main_window
    main_window = MainMenu()
    main_window.show()
    app.exec()

"""START MAIN MENU"""
def start_window():
    global main_menu_window
    main_menu_window = MainMenu()
    main_menu_window.show()

if __name__ == '__main__':
    open_app()

# open_app()
