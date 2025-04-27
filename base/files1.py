from pathlib import Path
from pprint import pp
from sys import path


script_dir = Path(path[0])
file_path = script_dir / 'literals.py'

file_obj = open(file_path, encoding='utf-8')

# >>> file_obj
# <_io.TextIOWrapper name='D:\\G-Doc\\TOP Academy\\Data Science\\521\\scripts\\base\\literals.py' mode='r' encoding='cp65001'>

text = file_obj.read()

file_obj.close()


file_obj = open(script_dir / 'in1.txt', encoding='utf-8')

text_lines = []
for line in file_obj:
    text_lines.append(line)

pp(text_lines, width=30)

# ['первая строчка\n',
#  'вторая строчка текста\n',
#  'третья\n',
#  'последняя']

file_obj.close()

