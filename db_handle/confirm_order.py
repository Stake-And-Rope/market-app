#!/usr/bin/python3
import sys
sys.path.append(r'.')
sys.path.append(r'..')
from db_handle import postgres_conn
# from pyqt5_gui import login

# postgres_conn.admin_client()
admin_cursor = postgres_conn.POSTGRES_CURSOR
admin_connection = postgres_conn.POSTGRES_CONNECTION

"""USER CLIENT TO THE POSTGRE DATABASE"""
# login.user_cursor.execute("SELECT current_user")
# current_user = login.user_cursor.fetchone()
# current_user = current_user[0].replace("_marketapp", "")
# print(f"From basket print: {current_user}")


def make_order():
    admin_cursor.execute(f"select products.product_id, products.product_name, \
		    products.category, products.single_price, products.quantity as av_qty, products.unit_of_measure, \
		    basket.product_id as basket_prodid, basket.product_name as basket_prodname, \
            basket.quantity as ord_qty from products inner join basket on products.product_id = basket.product_id \
            where basket.username = 'pesho';")
    basket_result = admin_cursor.fetchall()
    
    not_valid_items = []
    
    for i in basket_result:
        # print(f"item {i[0]} {i[1]} av_qty {i[4]} - ord_qty {i[7]}")
        if i[4] < i[8]:
            not_valid_items.append(f"{i[1]} {i[0]} not enough available quantity. Difference {abs(i[4] - i[8])} {i[5]}")
    
    print("\n".join(not_valid_items))


make_order()

"""WHAT THE JOIN QUERY RETURNS"""
# ('SKU-025512', 'Sunglasses1', 'Accessories', Decimal('45.99'), Decimal('41.00'), 'SKU-025512', 'Sunglasses1', Decimal('0.00'))