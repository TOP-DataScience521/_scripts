from psycopg import connect
from psycopg.conninfo import make_conninfo

from json import loads as json_loads
from pathlib import Path
from pprint import pp
from sys import path


sel_cnt_doc_vacations = '''
   select d.id,
          concat_ws(' ', last_name, first_name, patr_name) as "fio",
          count(v.id) as "vacations"
     from doctors as d
left join vacations as v
       on doctor_id = d.id
 group by d.id, "fio"
 order by "fio"
'''


dir_path = Path(path[0])
connection_config_path = dir_path / 'conn_conf.json'

config = json_loads(connection_config_path.read_text(encoding='utf-8'))

with connect(make_conninfo(**config)) as conn:
    with conn.cursor() as cursor:
        cursor.execute(sel_cnt_doc_vacations)
        columns = cursor.description
        data = cursor.fetchall()

columns = [r[0] for r in columns]

print(columns)
pp(data)

