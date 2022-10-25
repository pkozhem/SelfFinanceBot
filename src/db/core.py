""" ORM Core. """

import os
import sqlite3
from src.settings import BASE_DIR


connection = sqlite3.connect(os.path.join(BASE_DIR, "src/database/finance.db"))
cursor = connection.cursor()


def insert_data(table: str, field_values: dict) -> None:
    """ Inserts data in table using incoming data dictionary. """

    fields = ', '.join(field_values.keys())
    values = [tuple(field_values.values())]
    question_marks = ', '.join("?" * len(field_values.keys()))

    cursor.executemany(
        f"INSERT INTO {table} "
        f"({fields}) "
        f"VALUES ({question_marks})",
        values
    )
    connection.commit()


def delete_data(table: str, pk: int) -> None:
    """ Deletes a row in table by id. """

    cursor.execute(
        f"DELETE FROM {table} "
        f"WHERE id={pk}"
    )
    connection.commit()


def fetchall_data(table: str, fields: list[str]) -> list[dict]:
    """ This fetchall returns list of dictionaries instead of list of tuples. """

    fetchall_result = []
    fields_query = ', '.join(fields)
    cursor.execute(
        f"SELECT {fields_query} "
        f"FROM {table}"
    )
    rows = cursor.fetchall()

    for row in rows:
        row_in_dict = {}
        for index, field in enumerate(fields):
            row_in_dict[field] = row[index]
        fetchall_result.append(row_in_dict)

    return fetchall_result


def get_cursor() -> cursor:
    """ Returns database cursor. """
    return cursor


def _database_initialize() -> None:
    """ Initializes database. """

    with open(os.path.join(BASE_DIR, "src/database/finance.sql"), "r") as file:
        sql = file.read()
    cursor.executescript(sql)
    connection.commit()


def database_state() -> None:
    """ Checks if database exists. If it doesn't, creates it. """

    print("Checking database state: ")
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='Expense'")
    database_exists = cursor.fetchall()
    if database_exists:
        print("Database exists. Starting Bot ...")
        return
    print("Creating database ...")
    _database_initialize()
    print("Database created. Starting Bot ...")


# Explanation functions.

def fetchall_default() -> cursor:
    cursor.execute(
        "SELECT id_category, name, aliases "
        "FROM Category"
    )
    return cursor.fetchall()


def fetchall_explain() -> None:
    print(fetchall_default())
    print(fetchall_data("Category", "id_category, name, aliases".split(",")), "\n")
    return
