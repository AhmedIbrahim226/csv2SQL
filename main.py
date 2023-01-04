import argparse
import sys

parser = argparse.ArgumentParser(description="Multiplying X and Y.")

parser.add_argument("X", help="just given number", type=int)
parser.add_argument("Y", help="just given number", type=int)
group = parser.add_mutually_exclusive_group()
group.add_argument("-x", "--exit", help="exit from the program")
group.add_argument("-q", "--quit", help="quit from the program", action="store_true")




if __name__ == "__main__":
    if len(sys.argv) < 2: parser.print_help(); sys.exit()
    else: args = parser.parse_args()
    print(args.X * args.Y)
    print(args.quit)

# import pandas as pd
# import json
#
# df = pd.read_csv('data.csv')
#
#
# analysis = df.to_json()
# to_json = json.loads(analysis)
# print(to_json)

