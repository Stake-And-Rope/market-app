import sys
sys.path.append(r'.')
from db_handle import postgres_conn
import random, string


"""Init connection to the database"""
postgres_conn.admin_client()

def create_new_category():
    """Create ranomly generated category ID"""
    category_id = []
    for i in range(1, 7):
        category_id.append(random.choice(string.digits))
    category_id = 'CAT-' + ''.join(category_id)

    """Enter the category name"""
    category_name = input("Enter category name: ")
    
    """Save the category into the database"""
    postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO categories VALUES ('{category_id}', '{category_name}', '{0}', '{0}')")
    postgres_conn.POSTGRES_CONNECTION.commit()

def create_new_subcategory():
    """Create ranomly generated sub-category ID"""
    subcategory_id = []
    for i in range(1, 7):
        subcategory_id.append(random.choice(string.digits))
    subcategory_id = 'SUBCAT-' + ''.join(subcategory_id)
    
    """Enter the sub-category name"""
    subcategory_name = input("Enter the new subcategory name: ")
    
    """Set the parent category"""
    while True:
        parent_category = input("Enter the parent category: ")
        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT category_name FROM categories WHERE category_name = '{parent_category}'")
        result = postgres_conn.POSTGRES_CURSOR.fetchone()
        if result:
            postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO subcategories (subcategory_id, subcategory_name, total_items, parent_category) VALUES ('{subcategory_id}', '{subcategory_name}', '{0}', '{result[0]}')")
            postgres_conn.POSTGRES_CURSOR.execute(f"UPDATE categories SET total_subcategories = total_subcategories + 1 WHERE category_name = '{result[0]}'")
            postgres_conn.POSTGRES_CONNECTION.commit()
            break
        else:
            print(f"Wrong parent category name: {parent_category}. Try again.\n")
            continue

def create_new_items():
        """Create randomly generated item ID"""
        item_id = []
        for i in range(1, 7):
            item_id.append(random.choice(string.digits))
        item_id = 'SKU-' + ''.join(item_id)
        
        """Enter the item name"""
        item_name = input("Enter the new item name: ")
        
        """Single price"""
        single_price = float(input("Enter single price: "))
        
        """Enter quantity"""
        quantity = float(input("Enter quantity: "))

        """Enter unit of measure"""
        measure = input("Enter unit of measure: ")

        """Enter image url"""
        image_url = input("Enter an image url: ")
        
        """Set the item parent and child categories"""
        while True:
            parent_category = input("Enter the parent category: ")
            postgres_conn.POSTGRES_CURSOR.execute(f"SELECT category_name FROM categories WHERE category_name = '{parent_category}'")
            category_result = postgres_conn.POSTGRES_CURSOR.fetchone()
            if category_result:
                while True:
                    child_category = input("Enter the sub-category: ")
                    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT subcategory_name FROM subcategories WHERE subcategory_name = '{child_category}'")
                    subcategory_result = postgres_conn.POSTGRES_CURSOR.fetchone()
                    if subcategory_result:
                        postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO products (product_id, product_name, category, subcategory, single_price, quantity, unit_of_measure, image_url) "
                                                              f"VALUES ('{item_id}', '{item_name}', '{parent_category}', '{child_category}', '{single_price}', '{quantity}', '{measure}', '{image_url}')")
                        postgres_conn.POSTGRES_CURSOR.execute(f"UPDATE subcategories SET total_items = total_items + 1 WHERE subcategory_name = '{child_category}'")
                        postgres_conn.POSTGRES_CURSOR.execute(f"UPDATE categories SET total_items = total_items + 1 WHERE category_name = '{parent_category}'")
                        postgres_conn.POSTGRES_CONNECTION.commit()
                        break
                    else:
                        print(f"Child category name {child_category} not exists. Enter another child category.")
                        continue
                break
            else:
                print(f"Parent category name {parent_category} not exists. Enter another parent category.")
                continue


create_new_category()
create_new_subcategory()

create_new_items()