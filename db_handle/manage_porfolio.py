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

    """Calculates the total sub-categories / for new categories is 0 by default"""
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT COUNT (*) FROM subcategories WHERE parent_category = '{category_name}';")
    sub_categories_number = postgres_conn.POSTGRES_CURSOR.fetchone()
    
    """Calculates the total products inside the category / for new categories is 0 by default"""
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT COUNT (*) FROM products WHERE category = '{category_name}';")
    products_number = postgres_conn.POSTGRES_CURSOR.fetchone()
    
    """Save the category into the database"""
    postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO categories VALUES ('{category_id}', '{category_name}', '{sub_categories_number[0]}', '{products_number[0]}')")
    postgres_conn.POSTGRES_CONNECTION.commit()


def create_new_subcategory():
    """Create ranomly generated sub-category ID"""
    subcategory_id = []
    for i in range(1, 7):
        subcategory_id.append(random.choice(string.digits))
    subcategory_id = 'SUBCAT-' + ''.join(subcategory_id)
    
    """Enter the sub-category name"""
    subcategory_name = input("Enter the new subcategory name: ")

    """Calculates the total products inside the sub-category / for new sub-categories is 0 by default"""
    postgres_conn.POSTGRES_CURSOR.execute(f"SELECT COUNT (*) FROM products WHERE category = '{subcategory_name}';")
    products_number = postgres_conn.POSTGRES_CURSOR.fetchone()
    
    """Set the parent category"""
    while True:
        parent_category = input("Enter the parent category: ")
        postgres_conn.POSTGRES_CURSOR.execute(f"SELECT category_name FROM categories WHERE category_name = '{parent_category}'")
        result = postgres_conn.POSTGRES_CURSOR.fetchone()
        if len(result) > 0:
            postgres_conn.POSTGRES_CURSOR.execute(f"INSERT INTO subcategories (subcategory_id, subcategory_name, total_items, parent_category) VALUES ('{subcategory_id}', '{subcategory_name}', '{products_number[0]}', '{result[0]}')")
            postgres_conn.POSTGRES_CURSOR.execute(f"UPDATE categories SET total_subcategories = total_subcategories + 1 WHERE category_name = '{result[0]}'")
            postgres_conn.POSTGRES_CONNECTION.commit()
            break
        else:
            print(f"Wrong parent category name: {parent_category}. Try again.\n")
            continue

# create_new_category()
# create_new_subcategory()