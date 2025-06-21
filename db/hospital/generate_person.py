from datetime import date
from json import dump
from random import choice, sample, randrange as rr
from pathlib import Path
from pprint import pprint
from re import compile
from string import digits
from sys import path
from typing import Literal


SCRIPT_DIR = Path(path[0])

pattern1 = compile(r'\W+')

names = {
    'имена': {'мужской': [], 'женский': []},
    'отчества': {'мужской': [], 'женский': []},
    'фамилии': {'мужской': [], 'женский': []},
}
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
phone_codes = ['343', '495']


def load_data() -> None:
    m_names_path = SCRIPT_DIR / 'мужские_имена_отчества.txt'
    f_names_path = SCRIPT_DIR / 'женские_имена.txt'
    lastnames_path = SCRIPT_DIR / 'фамилии.txt'

    names['имена']['женский'] = f_names_path.read_text(encoding='utf-8').split('\n')
    
    raw_m_names = m_names_path.read_text(encoding='utf-8').split('\n')
    for line in raw_m_names:
        name, pat_m, pat_f, *_ = pattern1.split(line)
        names['имена']['мужской'] += [name]
        names['отчества']['мужской'] += [pat_m]
        names['отчества']['женский'] += [pat_f]

    raw_lastnames = lastnames_path.read_text(encoding='utf-8').split('\n')
    for line in raw_lastnames:
        try:
            lastn_m, lastn_f = line.split(', ')
        except ValueError:
            lastn_m = lastn_f = line
        names['фамилии']['мужской'] += [lastn_m]
        names['фамилии']['женский'] += [lastn_f]


def rand_date(from_year: int = -1, years: int = -1) -> tuple[int, int, int]:
    if from_year == -1:
        from_year = date.today().year
    if years == -1:
        years = date.today().year - from_year
    rand_year = rr(from_year, from_year+years)
    rand_month = rr(1, 13)
    leap_febr = rand_month == 2 and is_leap_year(rand_year)
    max_day = days[rand_month]+1 if leap_febr else days[rand_month]
    rand_day = rr(1, max_day+1)
    return date(rand_year, rand_month, rand_day)


def rand_phone(randomize_codes: bool = False):
    code = choice(phone_codes) if randomize_codes else phone_codes[0]
    return {
        'мобильный': f"+79{''.join(sample(digits, k=9))}",
        'городской': f"+7{code}{''.join(sample(digits, k=10-len(code)))}",
    }


def generate_person(
        sex: Literal['м', 'ж'] = None, 
        start_year: int = -1, 
        birth_period: int = 100
) -> dict:
    if sex is not None:
        match sex.lower():
            case 'м':
                sex = 'мужской'
            case 'ж':
                sex = 'женский'
    else:
        sex = choice(('мужской', 'женский'))
    return {
        'имя': choice(names['имена'][sex]),
        'отчество': choice(names['отчества'][sex]),
        'фамилия': choice(names['фамилии'][sex]),
        'пол': sex,
        'дата рождения': rand_date(start_year, birth_period),
        'мобильный': rand_phone()['мобильный'],
    }


def is_leap_year(year: int) -> bool:
    return year % 4 ==0 and year % 100 != 0 or year % 400 == 0


# def dump_rand_person_list(n: int = 1500):
#     person_list = [
#         generate_person()
#         for _ in range(n)
#     ]
#     filename = Path(__loader__.path).stem
#     with open(SCRIPT_DIR / f'{filename}.json', 'w', encoding='utf-8') as json_file:
#         dump(person_list, json_file, ensure_ascii=False, indent=2)

courses = ['русский язык', 'математика', 'история', 'литература', 'география', 'биология', 'физическая культура', 'технология', 'музыка', 'изобразительное искусство']
courses_short = ['русский язык', 'математика', 'история']

def dump_rand_school_classes():
    indent = ' '*4
    for _ in range(6):
        p = generate_person(None, 2013, 1)
        grades = {
            c: {
                f'{n} четверть': [rr(3, 6) for _ in range(rr(9, 16))]
                for n in range(1, 5)
            }
            for c in courses_short
        }
        print(
            '{',
            f"{indent}'фамилия': {p['фамилия']!r}, "
            f"'имя': {p['имя']!r}, "
            f"'отчество': {p['отчество']!r},",
            f"{indent}'пол': {p['пол']!r}, "
            f"'дата рождения': '{p['дата рождения']:%d.%m.%Y}',",
            f"{indent}'оценки': ",
            sep='\n'
        )
        pprint(grades, width=160, compact=True, sort_dicts=False)
        print('}')
        

load_data()



if __name__ == '__main__':
    pass
    # dump_rand_person_list()
    # dump_rand_school_classes()

