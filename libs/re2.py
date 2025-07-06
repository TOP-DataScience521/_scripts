from pathlib import Path
from pprint import pp
from re import compile, MULTILINE
from sys import path


script_dir = Path(path[0])
afisha_path = script_dir / 'afisha.txt'


afisha = afisha_path.read_text(encoding='utf-8')


pat_extract = compile(
    r'^(?P<concert_date>\d\d\.\d\d.\d\d\d\d)\. '
    r'(?P<concert_title>[^\.]+?)\. '
    r'(?P<composer>[а-яА-Я -]+?\.?(?:, [а-яА-Я -]+?\.)*?);? '
    r'(?P<production_year>\d{4})'
    r'(?:, (?P<comment>.+?))?$',
    flags=MULTILINE
)

matches = [
    mo.groupdict()
    for mo in pat_extract.finditer(afisha)
]

# >>> pp(matches[3165:3170])
# [{'concert_date': '27.01.1913',
#   'concert_title': '"Жизнь за царя" / "Иван Сусанин"',
#   'composer': 'Глинка М.',
#   'production_year': '1904',
#   'comment': None},
#  {'concert_date': '28.01.1913',
#   'concert_title': '"Миньон"',
#   'composer': 'Тома А.',
#   'production_year': '1912',
#   'comment': None},
#  {'concert_date': '29.01.1913',
#   'concert_title': '"Кармен"',
#   'composer': 'Бизе Ж.',
#   'production_year': '1913',
#   'comment': 'возобновление постановки 1898'},
#  {'concert_date': '30.01.1913',
#   'concert_title': '"Евгений Онегин"',
#   'composer': 'Чайковский П.',
#   'production_year': '1908',
#   'comment': None},
#  {'concert_date': '31.01.1913',
#   'concert_title': '"Садко"',
#   'composer': 'Римский-Корсаков Н.',
#   'production_year': '1906',
#   'comment': None}]

