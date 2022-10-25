import os
import sqlite3
from settings import BASE_DIR


connection = sqlite3.connect(os.path.join(BASE_DIR, "src/database/finance.db"))
cursor = connection.cursor()


def _initialize_database():
    with open(os.path.join(BASE_DIR, "src/database/finance.sql"), "r") as file:
        sql = file.read()
    cursor.executescript(sql)
    connection.commit()


def state_database():
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='Expense'")
    database_exists = cursor.fetchall()
    if database_exists:
        print("Database exists. Starting Bot ...")
        return
    print("Creating database ...")
    _initialize_database()
    print("Database created. Starting Bot ...")
