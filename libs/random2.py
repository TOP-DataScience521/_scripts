from random import (
    choice,
    sample
)

prob_60 = [False]*4 + [True]*6

prefix = 'к.т.н. '

names = ['Гиацинтов Харлампий Велимирович', 'Дубова Федора Аврамовна', 'Троицкая Анжела Викториновна', 'Златоумова Капитолина Альфредовна', 'Апраскин Филипп Ерофеевич', 'Сапфиров Пафнутий Денисович', 'Талисманова Габриэлла Диомидовна', 'Полковникова Жизель Иустиновна', 'Баронов Вонифатий Трофимович', 'Ивлеева Евтихия Евмениевна']


for name in sample(names, 5):
    name = (prefix if choice(prob_60) else '') + name
    print(name)

