from psycopg import connect
from psycopg.conninfo import make_conninfo

from json import loads as json_loads
from pathlib import Path
from sys import path


# демонстрационный пример — параметры подключения в исходном коде не должны быть прописаны явно!
connection_string = 'postgresql://postgres:root@localhost:5432/postgres'

conn = connect(connection_string)
cursor = conn.cursor()

print(conn, cursor, sep='\n')

cursor.close()
conn.close()


dir_path = Path(path[0])
connection_config_path = dir_path / 'conn_conf.json'

config = json_loads(connection_config_path.read_text(encoding='utf-8'))
connection_string = (
    f"postgresql://"
    f"{config['user']}:{config['password']}@"
    f"{config['host']}:{config['port']}/"
    f"{config['dbname']}"
)

with connect(connection_string) as conn:
    with conn.cursor() as cursor:
        print(conn, cursor, sep='\n')

