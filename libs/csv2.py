from pandas import read_csv

from datetime import datetime as dt
from pathlib import Path
from sys import path


example_csv_path = Path(path[0]) / 'example1.csv'

table = read_csv(example_csv_path, index_col=0)
table.columns = [
    dt.strptime(f'2024.{val}', '%Y.%m.%d').date()
    for val in table.columns
]


