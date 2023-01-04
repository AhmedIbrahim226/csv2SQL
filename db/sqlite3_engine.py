import sqlite3 as sqlite_db


def create_connection(path_to_db):
    con = sqlite_db.connect(path_to_db)
    return con
