import psycopg2 as postgres_db

def create_connection(user, password, host, dbname):
    con = postgres_db.connect(user=user, password=password, host=host, dbname=dbname, port=5432)
    return con
