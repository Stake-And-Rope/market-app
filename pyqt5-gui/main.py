#!/usr/bin/python3
"""DIRECTORY IMPORTS"""
import sys
sys.path.append(r'..')
from db_handle import postgres_conn

import login
login.init_app()
