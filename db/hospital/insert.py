from psycopg import connect
from psycopg.conninfo import make_conninfo

from json import loads as json_loads
from pathlib import Path
from sys import path

import generate
import queries


dir_path = Path(path[0])
connection_config_path = dir_path / 'conn_conf.json'

config = json_loads(connection_config_path.read_text(encoding='utf-8'))

with connect(make_conninfo(**config)) as conn:
    with conn.cursor() as cursor:
        cursor.executemany(queries.insert_departments, generate.departments)
        cursor.executemany(queries.insert_wards, generate.wards)
        cursor.executemany(queries.insert_sponsors, generate.sponsors)
        cursor.executemany(queries.insert_donations, generate.donations)
        cursor.executemany(queries.insert_doctors, generate.doctors)
        cursor.executemany(queries.insert_vacations, generate.vacations)
        cursor.executemany(queries.insert_specializations, generate.specializations)
        cursor.executemany(queries.insert_doctors_specs, generate.doctors_specs)
        conn.commit()

