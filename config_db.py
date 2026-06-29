import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",      # whatever your password is
    "database": "careers_db"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)