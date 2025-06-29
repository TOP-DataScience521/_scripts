from pathlib import Path
from pprint import pp
from sqlite3 import connect
from sys import path


script_dir = Path(path[0])
db_path = script_dir / 'test_db.sqlite3'


select_t1 = '''select * from t1'''
select_t2 = '''select * from t2'''

# объединение посредством сопоставления каждого кортежа данных одной таблицы каждому кортежу данных другой таблицы (декартово произведение)
select_t1_cartesian_t2 = '''select * from t1 join t2'''

# внутреннее объединение, использующее связанные одноимённые (!) столбцы
select_t1_inner_join_t2 = '''
select *
  from t1
  join t2
 using (t1_id)
'''
# внутреннее объединение с явным выражением связи и дополнительной фильтрацией
select_t1_inner_join_t2 = '''
select *
  from t1
  join t2
    on t1.t1_id = t2.t1_id
   and t1.t1_id = 1
'''

# внешнее объединение слева — из таблицы, расположенной слева от оператора объединения (t1) будут взяты кортежи данных, не сопоставленные ничему
select_t1_left_join_t2 = '''
   select * 
     from t1 
left join t2 
       on t1.t1_id = t2.t1_id
'''
# внешнее объединение справа — из таблицы, расположенной справа от оператора объединения (t1) будут взяты кортежи данных, не сопоставленные ничему
select_t2_right_join_t1 = '''
    select * 
      from t2
right join t1
        on t1.t1_id = t2.t1_id
'''

select_t1_right_join_t2 = '''
    select * 
      from t1
right join t2
        on t1.t1_id = t2.t1_id
'''
select_t2_left_join_t1 = '''
    select * 
      from t1
right join t2
        on t1.t1_id = t2.t1_id
'''

# полное внешнее объединение — кортежи данных, не сопоставленные ничему, берутся из обеих таблиц
select_t1_full_join_t2 = '''
   select * 
     from t1
full join t2
       on t1.t1_id = t2.t1_id
'''


with connect(db_path) as conn:
    cursor = conn.cursor()
    # отправка запроса движку СУБД
    cursor.execute(select_t1_full_join_t2)
    # извлечение полученных данных из буфера курсора
    columns = [r[0] for r in cursor.description]
    data = cursor.fetchall()
    
    print(columns)
    pp(data)

