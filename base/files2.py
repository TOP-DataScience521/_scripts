from pathlib import Path
from sys import path


script_dir = Path(path[0])
filein_path = script_dir / 'in1.txt'
fileout_path = script_dir / 'out1.txt'


with open(filein_path, encoding='utf-8') as filein:
    text_lines = [
        line.rstrip()
        for line in filein
    ]

text_lines[-1] = 'четвёртая строчка текста'
text_lines.append('пятая строчка')

text = '\n'.join(text_lines)

with open(fileout_path, 'w', encoding='utf-8') as fileout:
    fileout.write(f'{text}\n')

