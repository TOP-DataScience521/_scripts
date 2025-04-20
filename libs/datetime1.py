from datetime import (
    date,
    datetime as dt, 
    timedelta as td,
)


print(f'{date = }\n{dt = }\n{td = }\n')

course_start = date(2025, 3, 1)
course_end = date(2026, 1, 17)

class_start = dt(2025, 4, 19, 12)
class_end = dt(2025, 4, 19, 15)

print(
    f'{course_end - course_start = }\n'
    f'{class_end - class_start = }\n'
)


class_start = dt.strptime('20.04.25 12:00', '%d.%m.%y %H:%M')
current_dt = dt.now()

print(
    f'{class_start = } ({class_start:%d.%m.%Y г. %H час %M мин})',
    f'{current_dt = } ({current_dt:%d.%m.%Y г. %H час %M мин})',
    f'{current_dt - class_start = !s}',
    sep='\n'
)
