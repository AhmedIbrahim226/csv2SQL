from .sqlite3_engine import create_connection as sqlite_create_connection
from cs_v.csv_operations import read_csv_file


class Queries(object):

    def __init__(self, engine, csv_file_path, table, path=None):
        if engine == "sqlite":
            self.to_sqlite_db(path, csv_file_path, table)
        elif engine == "postgres":
            self.to_postgres_db()

    @staticmethod
    def to_sqlite_db(path, csv_file_path, table):
        con = sqlite_create_connection(path_to_db=path)
        data = read_csv_file(path_to_csv=csv_file_path)
        data.to_sql(table, con=con, if_exists='append', index=False)
        con.close()

    @staticmethod
    def to_postgres_db():
        pass

query = Queries