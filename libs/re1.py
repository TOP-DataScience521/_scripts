from re import compile


# формат даты: ДД.ММ.ГГГГ
pat_date = compile(r'[0123456789][0-9]\.\d\d\.\d{4}')

text = '''
01.01.1893. "Жизнь за царя" / "Иван Сусанин". Глинка М. 1892
03.01.1893. "Пиковая дама". Чайковский П. 1891
04.01.1893. "Жизнь за царя" / "Иван Сусанин". Глинка М. 1892
07.01.1893. "Лоэнгрин". Вагнер Р. 1889
08.01.1893. "Демон". Рубинштейн А. 1879
11.01.1893. "Гугеноты". Мейербер Д. 1879
12.01.1893. "Евгений Онегин". Чайковский П. 1889
14.01.1893. "Аида". Верди Д. 1892
15.01.1893. "Пиковая дама". Чайковский П. 1891
17.01.1893. "Ролла". Симон А. 1892
18.01.1893. "Роберт-дьявол". Мейербер Д. 1887
20.01.1893. "Травиата". Верди Д. 1872
22.01.1893. "Гугеноты". Мейербер Д. 1879
25.01.1893. "Русалка". Даргомыжский А. 1865
26.01.1893. "Снегурочка". Римский-Корсаков Н. 1893
28.01.1893. "Евгений Онегин". Чайковский П. 1889
29.01.1893. "Снегурочка". Римский-Корсаков Н. 1893
31.01.1893. "Снегурочка". Римский-Корсаков Н. 1893
'''

test = '12.34.5678.90.12.4567894.12.5679.2'

# >>> pat_date.search(text)
# <re.Match object; span=(1, 11), match='01.01.1893'>
# >>>
# >>> pat_date.match(text)
# >>>
# >>> pat_date.fullmatch(text)
# >>>
# >>> pat_date.findall(text)
# ['01.01.1893', '03.01.1893', '04.01.1893', '07.01.1893', '08.01.1893', '11.01.1893', '12.01.1893', '14.01.1893', '15.01.1893', '17.01.1893', '18.01.1893', '20.01.1893', '22.01.1893', '25.01.1893', '26.01.1893', '28.01.1893', '29.01.1893', '31.01.1893']
# >>>
# >>> pat_date.finditer(text)
# <callable_iterator object at 0x000002902E388400>
# >>>
# >>> list(pat_date.finditer(text))
# [<re.Match object; span=(1, 11), match='01.01.1893'>, <re.Match object; span=(62, 72), match='03.01.1893'>, <re.Match object; span=(109, 119), match='04.01.1893'>, <re.Match object; span=(170, 180), match='07.01.1893'>, <re.Match object; span=(209, 219), match='08.01.1893'>, <re.Match object; span=(249, 259), match='11.01.1893'>, <re.Match object; span=(290, 300), match='12.01.1893'>, <re.Match object; span=(339, 349), match='14.01.1893'>, <re.Match object; span=(373, 383), match='15.01.1893'>, <re.Match object; span=(420, 430), match='17.01.1893'>, <re.Match object; span=(455, 465), match='18.01.1893'>, <re.Match object; span=(501, 511), match='20.01.1893'>, <re.Match object; span=(539, 549), match='22.01.1893'>, <re.Match object; span=(580, 590), match='25.01.1893'>, <re.Match object; span=(624, 634), match='26.01.1893'>, <re.Match object; span=(675, 685), match='28.01.1893'>, <re.Match object; span=(724, 734), match='29.01.1893'>, <re.Match object; span=(775, 785), match='31.01.1893'>]

# >>> pat_date.findall(test)
# ['12.34.5678', '90.12.4567', '94.12.5679']


pat_date_realistic = compile(
    r'(0[1-9]|[12][0-9]|3[01])\.'
    r'(0[1-9]|1[012])\.'
    r'[12]\d{3}'
)
# >>> print(pat_date_realistic.pattern)
# (0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.[12]\d{3}

# >>> pat_date_realistic.search(text)
# <re.Match object; span=(1, 11), match='01.01.1893'>
# >>>
# >>> pat_date_realistic.match(text)
# >>>
# >>> pat_date_realistic.fullmatch(text)
# >>>
# >>> pat_date_realistic.findall(text)
# [('01', '01'), ('03', '01'), ('04', '01'), ('07', '01'), ('08', '01'), ('11', '01'), ('12', '01'), ('14', '01'), ('15', '01'), ('17', '01'), ('18', '01'), ('20', '01'), ('22', '01'), ('25', '01'), ('26', '01'), ('28', '01'), ('29', '01'), ('31', '01')]
# >>>
# >>> list(pat_date_realistic.finditer(text))
# [<re.Match object; span=(1, 11), match='01.01.1893'>, <re.Match object; span=(62, 72), match='03.01.1893'>, <re.Match object; span=(109, 119), match='04.01.1893'>, <re.Match object; span=(170, 180), match='07.01.1893'>, <re.Match object; span=(209, 219), match='08.01.1893'>, <re.Match object; span=(249, 259), match='11.01.1893'>, <re.Match object; span=(290, 300), match='12.01.1893'>, <re.Match object; span=(339, 349), match='14.01.1893'>, <re.Match object; span=(373, 383), match='15.01.1893'>, <re.Match object; span=(420, 430), match='17.01.1893'>, <re.Match object; span=(455, 465), match='18.01.1893'>, <re.Match object; span=(501, 511), match='20.01.1893'>, <re.Match object; span=(539, 549), match='22.01.1893'>, <re.Match object; span=(580, 590), match='25.01.1893'>, <re.Match object; span=(624, 634), match='26.01.1893'>, <re.Match object; span=(675, 685), match='28.01.1893'>, <re.Match object; span=(724, 734), match='29.01.1893'>, <re.Match object; span=(775, 785), match='31.01.1893'>]

# >>> pat_date_realistic.findall(test)
# []


pat_date_realistic_2 = compile(
    r'(?P<day>0[1-9]|[12][0-9]|3[01])\.'
    r'(?P<month>0[1-9]|1[012])\.'
    r'(?P<year>[12]\d{3})'
)

# >>> mo = pat_date_realistic_2.search(text, 60)
# >>> mo
# <re.Match object; span=(62, 72), match='03.01.1893'>
# >>>
# >>> mo.start(), mo.end()
# (62, 72)
# >>>
# >>> mo.span()
# (62, 72)
# >>>
# >>> mo.group()
# '03.01.1893'
# >>>
# >>> mo.group(0)
# '03.01.1893'
# >>>
# >>> mo.group(1)
# '03'
# >>>
# >>> mo.group(2)
# '01'
# >>>
# >>> mo.group(3)
# '1893'
# >>>
# >>> mo.group(4)
# IndexError: no such group
# >>>
# >>> mo.group('day')
# '03'
# >>>
# >>> mo.group('month')
# '01'
# >>>
# >>> mo.group('year')
# '1893'
# >>>
# >>> mo.group(1) == mo.group('day') == mo[1] == mo['day']
# True
# >>>
# >>> mo.group(2) == mo.group('month') == mo[2] == mo['month']
# True
# >>>
# >>> mo.group(3) == mo.group('year') == mo[3] == mo['year']
# True
# >>>
# >>>
# >>> mo.groups()
# ('03', '01', '1893')


# >>> pat_date_realistic_2.findall(text, 60)
# [('03', '01', '1893'), ('04', '01', '1893'), ('07', '01', '1893'), ('08', '01', '1893'), ('11', '01', '1893'), ('12', '01', '1893'), ('14', '01', '1893'), ('15', '01', '1893'), ('17', '01', '1893'), ('18', '01', '1893'), ('20', '01', '1893'), ('22', '01', '1893'), ('25', '01', '1893'), ('26', '01', '1893'), ('28', '01', '1893'), ('29', '01', '1893'), ('31', '01', '1893')]


