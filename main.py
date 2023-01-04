import argparse
import sys
from db.queries import query

parser = argparse.ArgumentParser(description="Csv2SQL.")

parser.add_argument("csv_file_path", help="The path of cs_v file.")
parser.add_argument("db_engine", help="Database db.", choices=['sqlite', 'postgres'])
parser.add_argument("table", help="The table name.")
parser.add_argument("--path", help="The path of sqlite db file.")



if __name__ == "__main__":
    if len(sys.argv) < 2: parser.print_help(); sys.exit()
    else: args = parser.parse_args()

    if args.db_engine == 'sqlite' and not args.path:
        parser.error('Please specify --path argument.')

    if args.db_engine == "sqlite":
        query(args.db_engine, args.csv_file_path, args.table, args.path)
