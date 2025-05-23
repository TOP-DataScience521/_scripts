from pprint import pp
from uuid import uuid4


persons = [
    'Гиацинтов Харлампий Велимирович', 
    'Дубова Федора Аврамовна', 
    'Троицкая Анжела Викториновна', 
    'Златоумова Капитолина Альфредовна', 
    'Апраскин Филипп Ерофеевич', 
    'Сапфиров Пафнутий Денисович', 
    'Талисманова Габриэлла Диомидовна', 
    'Полковникова Жизель Иустиновна', 
    'Баронов Вонифатий Трофимович', 
    'Ивлеева Евтихия Евмениевна'
]

personal_data = {
    uuid4(): p
    for p in persons
}

pp(personal_data, width=100)

# {UUID('05b682b0-1188-49ee-b881-2441cb249583'): 'Гиацинтов Харлампий Велимирович',
#  UUID('7d6fb5d6-595d-4ad0-9a01-a83416e26ba6'): 'Дубова Федора Аврамовна',
#  UUID('fc43e2e7-617c-4727-9c82-5a5daa483382'): 'Троицкая Анжела Викториновна',
#  UUID('af1994ec-0229-4714-8557-21fc13ec44bf'): 'Златоумова Капитолина Альфредовна',
#  UUID('473b251c-e8af-4d31-9acb-7f884f5d401b'): 'Апраскин Филипп Ерофеевич',
#  UUID('952207c8-cd03-46d6-af86-d0452cbb7ea2'): 'Сапфиров Пафнутий Денисович',
#  UUID('8069fd7c-8583-4ecf-844a-085f2716c89d'): 'Талисманова Габриэлла Диомидовна',
#  UUID('dac9e9c0-8572-4301-9fd7-bef4e7994e6e'): 'Полковникова Жизель Иустиновна',
#  UUID('29989b7d-4cdd-4f99-a365-8f9368636e5d'): 'Баронов Вонифатий Трофимович',
#  UUID('14884612-53b0-47b6-b364-b40651a95397'): 'Ивлеева Евтихия Евмениевна'}

