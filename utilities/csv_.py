import pandas as pd

def read_csv_file(path_to_csv: str):
    data = pd.read_csv(path_to_csv)
    columns = [column.strip().replace(' ', '_') for column in data.columns]
    return data, columns
