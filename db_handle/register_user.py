import sys
sys.path.append(r'.')
from db_handle import postgres_conn

postgres_conn.admin_client()

"""Create new user in pg_user table and grant him customers_marketapp role with privileges to read and update tables on the database(only public schemas)."""
def create_user(username, passwd):
    try:
        postgres_conn.POSTGRES_CURSOR.execute(f"CREATE USER {username}_marketapp WITH PASSWORD '{passwd}'") # <--{username}_marketapp will distinguish the users for market-app DB from the rest of the users
        postgres_conn.POSTGRES_CURSOR.execute(f"GRANT customers_marketapp TO {username}_marketapp")  
        postgres_conn.POSTGRES_CONNECTION.commit()
    except (Exception) as error:
        print("Error creating new user")
    