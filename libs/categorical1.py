from pandas import read_csv

from pathlib import Path
from pprint import pp
from sys import path


script_dir = Path(path[0])

data = read_csv(script_dir / 'ru-cities.csv')

columns_mask = ['lat', 'lng', 'region', 'population']
rows_mask = [True]*data.shape[0]

data_filt = data.loc[rows_mask, columns_mask]


region_map = {
    r: i
    for i, r in enumerate(data_filt['region'].value_counts().index)
}

def mapper(row):
    # breakpoint()
    return region_map[row['region']]

data_filt_enc = data_filt.copy()
data_filt_enc['region'] = data_filt_enc.apply(mapper, axis=1)


data_filt_enc2 = data_filt.copy()
data_filt_enc2 = data_filt_enc2.astype({'region': 'category'})


