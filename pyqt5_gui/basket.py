#!/usr/bin/python3

# Import PyQt5 Engine
from PyQt5.QtWidgets import (QWidget,
                             QPushButton,
                             QLabel,
                             QScrollArea,
                             QHBoxLayout,
                             QVBoxLayout,
                             QSpinBox, QMessageBox,
                             )

from PyQt5.QtGui import *
from PyQt5.QtCore import *
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

    def redirect_to_insert_to_postgre_func(prod_id, prod_name):
        return lambda: insert_into_favourite_products(prod_id, prod_name)

    def redirect_to_delete_postgres_func(c_product_name):
        return lambda: delete_from_basket(c_product_name)

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

        current_favourites_button = QPushButton()
        current_favourites_button.setToolTip("Add to favourites")
        current_favourites_button.setFixedWidth(35)
        current_favourites_button.setFixedHeight(35)
        current_favourites_button.setIcon(QIcon(r'../img/favorite.png'))
        current_favourites_button.setIconSize(QSize(30, 30))
        current_favourites_button.clicked.connect(redirect_to_insert_to_postgre_func(product_id, product_name))

        current_remove_button = QPushButton()
        current_remove_button.setToolTip("Remove from basket")
        current_remove_button.setFixedSize(35, 35)
        current_remove_button.setIcon(QIcon(r"../img/trash.png"))
        current_remove_button.setIconSize(QSize(30, 30))
        current_remove_button.clicked.connect(redirect_to_delete_postgres_func(product_name))

        current_spin_box = QSpinBox()
        current_spin_box.setToolTip("Change quantity")
        current_spin_box.setValue(int(quantity))

        current_buttons_layout.addWidget(current_favourites_button)
        current_buttons_layout.addWidget(current_remove_button)
        current_buttons_layout.addWidget(current_spin_box)

        current_horizontal_layout.insertWidget(0, product_image)
        current_horizontal_layout.addWidget(current_sku)
        current_horizontal_layout.addWidget(current_description)
        current_horizontal_layout.addLayout(current_buttons_layout)

        basket_menu_h_layout.addLayout(current_horizontal_layout)
        basket_menu_h_layout.addStretch()
        basket_menu_h_layout.addSpacing(20)
    
    """HORIZONTAL LAYOUT FOR THE BOTTOM BUTTONS"""
    order_buttons_layout = QHBoxLayout()
    order_buttons_layout.setAlignment(Qt.AlignRight)
    make_order_button = QPushButton()
    make_order_button.setText("Confirm Order")
    make_order_button.setFixedSize(130, 50)
    make_order_button.setProperty("class", "log_out_button")
    order_buttons_layout.addWidget(make_order_button)
    basket_menu_h_layout.addLayout(order_buttons_layout)

    basket_widget.setLayout(basket_menu_h_layout)

    basket_menu_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    basket_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    basket_menu_scroll.setWidgetResizable(True)
    basket_menu_scroll.setWidget(basket_widget)

    def insert_into_favourite_products(curr_id, curr_product_name):
        admin_cursor.execute(
            f"SELECT * FROM favourite_products WHERE product_id = '{curr_id}' AND username = '{current_user}'")
        result = admin_cursor.fetchall()

        """HERE WE SELECT THE AVAILABLE QUANTITY OF THE PRODUCT AND SEE IF WE CAN ADD IT TO FAVOURITES"""
        admin_cursor.execute(f"SELECT quantity FROM products WHERE product_id='{curr_id}';")
        available_quantity = admin_cursor.fetchone()

        if result:
            error_message_box("Product already exists in favorites.")
        else:
            admin_cursor.execute(
                f"INSERT INTO favourite_products VALUES ('{current_user}', '{curr_id}', '{curr_product_name}')")
            admin_connection.commit()

    def error_message_box(message):
        error_msg_box = QMessageBox()
        error_msg_box.setIcon(QMessageBox.Warning)
        error_msg_box.setText(message)
        error_msg_box.setWindowTitle("Info Message")
        error_msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box = error_msg_box.exec()

        return msg_box

    def delete_from_basket(curr_product_name):
        admin_cursor.execute(f"DELETE FROM basket WHERE product_name = '{curr_product_name}' AND username = '{current_user}';")
        admin_connection.commit()
        print("Deleted")

    return basket_menu_scroll
