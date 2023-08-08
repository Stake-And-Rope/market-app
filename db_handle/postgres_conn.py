#!/usr/bin/python3

import psycopg2, sshtunnel
from decouple import config


POSTGRES_CURSOR = ''
POSTGRES_CONNECTION = ''

USER_POSTGRES_CURSOR = ''
USER_POSTGRES_CONNECTION = ''

def admin_client():
    global POSTGRES_CURSOR
    global POSTGRES_CONNECTION

    """Read Linux Debian Server Credentials from env file"""
    linux_username = config('LINUX_USERNAME')
    linux_password = config('LINUX_PASSWORD')
    linux_ip_address = config('LINUX_IP_ADDRESS')

    """Read Database Server Credentials from env file"""
    database_username = config('DATABASE_USERNAME')
    database_password = config('DATABASE_PASSWORD')
    database_host = config('DATABASE_HOST')
    database_name = config('DATABASE_NAME')

    
    """Initiate SSH Tunnel to the Linux Server"""
    try:
        tunnel = sshtunnel.SSHTunnelForwarder(
                (str(linux_ip_address), 22),
                ssh_username = str(linux_username),
                ssh_password = str(linux_password),
                remote_bind_address = ('127.0.0.1', 5432)
                )
        # print("SSH connection has been established!")
        tunnel.start()
    except (Exception) as error:
        print("SSH connection failed!")

    """Initiate DB connection to Postgres(as superuser) and create DB cursor ready to execute SQL queries"""
    try:
        db_client = psycopg2.connect(
                user = str(database_username),
                password = str(database_password),
                host = str(database_host),
                dbname = str(database_name)
                )
        cursor = db_client.cursor()
        # cursor.execute("SELECT version()")
        print("Admin database connection established!")
    except (Exception) as error:
        print("Database connection failed!")


    """Export the global variables"""
    POSTGRES_CURSOR = cursor
    POSTGRES_CONNECTION = db_client
    """Close connection to the Linux Server and the Postgres DB. This two lines should be commented in production environment"""

def user_client(username, passwd):
    global USER_POSTGRES_CURSOR
    global USER_POSTGRES_CONNECTION
    
    """Read Linux Debian Server Credentials from env file"""
    linux_username = config('LINUX_USERNAME')
    linux_password = config('LINUX_PASSWORD')
    linux_ip_address = config('LINUX_IP_ADDRESS')
    
    """Read Database Server Credentials from env file"""
    database_username = username
    database_password = passwd
    database_host = config('DATABASE_HOST')
    database_name = config('DATABASE_NAME')
    
    """Initiate SSH Tunnel to the Linux Server"""
    try:
        tunnel = sshtunnel.SSHTunnelForwarder(
                (str(linux_ip_address), 22),
                ssh_username = str(linux_username),
                ssh_password = str(linux_password),
                remote_bind_address = ('127.0.0.1', 5432)
                )
        # print("SSH connection has been established!")
        tunnel.start()
    except (Exception) as error:
        print("SSH connection failed!")

    """Initiate DB connection to Postgres(as superuser) and create DB cursor ready to execute SQL queries"""
    try:
        user_db_client = psycopg2.connect(
                user = str(database_username) + "_marketapp",
                password = str(database_password),
                host = str(database_host),
                dbname = str(database_name)
                )
        user_cursor = user_db_client.cursor()
        # user_cursor.execute("SELECT version()")
        print("Client database connection established!")
    except (Exception) as error:
        raise Exception("Database connection failed!")
        
    

    USER_POSTGRES_CURSOR = user_cursor
    USER_POSTGRES_CONNECTION = user_db_client
    
admin_client()
# user_database = user_client()

