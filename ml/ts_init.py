from pandas import read_csv

from pathlib import Path
from sys import path


script_dir = Path(path[0])

births = read_csv(
    script_dir / 'ts_births.csv', 
    index_col='date',
    date_format='%Y-%m-%d',
)
births_ = read_csv(
    script_dir / 'ts_births_.csv', 
    index_col='date',
    date_format='%Y-%m-%d',
)
passengers = read_csv(
    script_dir / 'ts_passengers.csv', 
    index_col=0,
    date_format='%Y-%m'
)
online = read_csv(
    script_dir / 'ts_hour-online.csv', 
    index_col='Time',
    date_format='%m/%d/%y %H:%M'
)

