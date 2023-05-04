
import sys
sys.path.append(r'.')
from db_handle import postgres_conn

postgres_conn.admin_client()

def create_user(username, passwd):
    postgres_conn.POSTGRES_CURSOR.execute(f"CREATE USER {username} WITH PASSWORD '{passwd}'")
    postgres_conn.POSTGRES_CONNECTION.commit()