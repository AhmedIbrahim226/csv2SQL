from .sqlite3_engine import create_connection as sqlite_create_connection
from .postgresql_engine import create_connection as postgres_create_connection
from utilities.csv_ import read_csv_file


class Queries(object):

    def __init__(self, engine, csv_file_path, table, dbpath=None, connection_url=None):
        if engine == "sqlite":
            self.to_sqlite_db(dbpath, csv_file_path, table)
        elif engine == "postgres":
            self.to_postgres_db(csv_file_path=csv_file_path, connection_url=connection_url, table=table)

    @staticmethod
    def to_sqlite_db(dbpath, csv_file_path, table):
        con = sqlite_create_connection(path_to_db=dbpath)
        data = read_csv_file(path_to_csv=csv_file_path)
        data.to_sql(table, con=con, if_exists='append', index=False)
        con.close()

    @staticmethod
    def to_postgres_db(csv_file_path, connection_url, table):
        con_s = connection_url.split(":")

        user = con_s[1][2:]
        pass_n_host_n_dbname = con_s[2].split("@")
        _pass = pass_n_host_n_dbname[0]
        host_n_dbname = pass_n_host_n_dbname[1]
        host = host_n_dbname.split("/")[0]
        dbname = host_n_dbname.split("/")[1]

        con = postgres_create_connection(user=user, password=_pass, host=host, dbname=dbname)
        data = read_csv_file(path_to_csv=csv_file_path)
        data.to_sql(table, con=con, if_exists='append', index=False)
        con.close()

query = Queries