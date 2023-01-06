import psycopg2 as postgres_db


def create_connection(user, password, host, dbname):
    conn = postgres_db.connect(user=user, password=password, host=host, dbname=dbname, port=5432)
    cur = conn.cursor()

    return conn, cur


def create_table_if_exists(cur, table: str, columns):
    cur.execute(f"""CREATE TABLE IF NOT EXISTS "{table}" ({' varchar,'.join(columns)+' varchar'});""")


def insert_values(conn, cur, table: str, values):
    values = map(lambda v: str(tuple(v)), values)
    cur.execute(f"""INSERT INTO "{table}" VALUES {', '.join(list(values))};""")
    conn.commit()
    cur.close()
    conn.close()
