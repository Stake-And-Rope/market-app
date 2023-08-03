#!/usr/bin/python3
"""DIRECTORY IMPORTS"""
import sys
sys.path.append(r'..')
from db_handle import postgres_conn


        
"""INIT CONNECTION TO THE DATABASE"""
# admin_database = postgres_conn.admin_database
# user_database = postgres_conn.user_database

import login
login.init_app()
