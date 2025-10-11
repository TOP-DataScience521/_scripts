from datetime import datetime as dt
from pathlib import Path
from pprint import pp
from sys import path


example_csv_path = Path(path[0]) / 'example1.csv'
text = example_csv_path.read_text(encoding='utf-8')

lines = text.split('\n')
table = []
for row in lines:
    table.append(row.split(','))

table[0] = [
    dt.strptime(f'2024.{val}', '%Y.%m.%d').date() if val else val
    for val in table[0]
]
for i in range(1, len(table)):
    for j in range(1, len(table[0])):
        table[i][j] = int(table[i][j])

pp(table)

