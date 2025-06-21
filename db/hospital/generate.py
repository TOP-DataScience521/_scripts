from datetime import date, timedelta as td
from random import randrange as rr, uniform, choice

import generate_person as person


prob_80 = [False]*2 + [True]*8
prob_90 = [False] + [True]*9

departments = [
    ("Отделение общей терапии",),
    ("Неврологическое отделение",),
    ("Кардиологическое отделение",),
    ("Отделение функциональной диагностики",),
    ("Реанимация и интенсивная терапия",),
    ("Токсикологическое отделение",),
    ("Физиотерапевтическое отделение",),
]
sponsors = [
    ("Детский паллиатив",), 
    ("Обнимая небо",), 
    ("Фонд имени Анжелы Вавиловой",),
    ("Защити жизнь",), 
    ("Близко к сердцу",), 
    ("София",), 
    ("ДоброДомик",), 
    ("Апельсин",), 
    ("Преодолей-ка",), 
    ("Близкие другие",), 
    ("Галчонок",), 
    ("Перспективы",), 
    ("Жизненный путь",),
]
specializations = [
    ("Анестезиолог",),
    ("Гастроэнтеролог",),
    ("Дерматолог",),
    ("Диетолог",),
    ("Иммунолог",),
    ("Кардиолог",),
    ("Невролог",),
    ("Нарколог",),
    ("Онколог",),
    ("Ортопед",),
    ("Оториноларинголог",),
    ("Офтальмолог",),
    ("Реаниматолог",),
    ("Ревматолог",),
    ("Стоматолог",),
    ("Терапевт",),
    ("Травматолог",),
    ("Уролог",),
    ("Хирург",),
    ("Эндокринолог",),
]

wards = []
for fk, dep in enumerate(departments, 1):
    for n in range(1, rr(3, 6)):
        ward = ''.join(
            w[0].upper() 
            for w in dep[0].split() 
            if len(w) > 1
        )
        wards.append((fk, f'{ward}-{n}'))

# print(*wards, sep=',\n')


donations = []
for _ in range(50):
    date = person.rand_date(from_year=2014)
    donations.append((
        rr(1, 14),
        rr(1, 8),
        f'{date:%Y-%m-%d}',
        round(uniform(12, 795)*1000, 2),
    ))

# print(*donations, sep=',\n')


doctors = []
for _ in range(70):
    pers = person.generate_person()
    premium = round(uniform(100, 530)*100, 2) if choice(prob_80) else 0.0
    doctors.append((
        rr(1, 8),
        pers['фамилия'],
        pers['имя'],
        pers['отчество'],
        round(uniform(340, 780)*100, 2),
        premium,
    ))

# print(*doctors, sep=',\n')


doctors_specs = []
for _ in range(50):
    spec_cnt = 1 if choice(prob_90) else 2
    for _ in range(spec_cnt):
        doctors_specs.append((
            rr(1, 71),
            rr(1, 21),
        ))

# print(*doctors_specs, sep=',\n')


vacations = []
for _ in range(250):
    start_date = person.rand_date(from_year=2017)
    end_date = start_date + td(days=rr(5, 22))
    vacations.append((
        rr(1, 71),
        f'{start_date:%Y-%m-%d}',
        f'{end_date:%Y-%m-%d}',
    ))

# print(*vacations, sep=',\n')

