import argparse
import sys
from db.queries import query
from utilities.regex import match_postgres_con_regex as con_regex


parser = argparse.ArgumentParser(description="Csv2SQL.")
parser.add_argument("csv_file_path", help="The path of utilities file.")
parser.add_argument("db_engine", help="Database (db type).", choices=['sqlite', 'postgres'])
parser.add_argument("table", help="The table name.")
parser.add_argument("-p", "--path", help="The path of sqlite db file.")
parser.add_argument("-c", "--connection", help="The postgres connection url (postgresql://user:pass@host/dbname).")



if __name__ == "__main__":
    if len(sys.argv) < 2: parser.print_help(); sys.exit()
    else: args = parser.parse_args()

    if args.db_engine == 'sqlite' and not args.path:
        parser.error('Please specify -p --path argument.')
    elif args.db_engine == 'postgres' and not args.connection:
        parser.error('Please specify -c --connection argument.')

    if args.db_engine == "sqlite":
        query(engine=args.db_engine, csv_file_path=args.csv_file_path, table=args.table, dbpath=args.path)
    elif args.db_engine == 'postgres':
        is_match =  con_regex(args.connection)
        if not is_match : parser.error('Postgres connection expression does\'t as required.')
        query(engine=args.db_engine, csv_file_path=args.csv_file_path, table=args.table, connection_url=args.connection)
