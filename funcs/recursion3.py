data1 = [
    (1, 2, 3),
    (4, 5, 6),
]
data2 = [
    [
        (1, 2, 3),
        (4, 5, 6),
    ],
    [
        (7, 8, 9),
        (10, 11, 12),
    ],
]
data3 = [
    (
        [
            {1, 2, 3},
            {4, 5, 6},
        ],
        [
            {7, 8, 9},
            {10, 11, 12},
        ],
    ),
    (
        [
            {13, 14, 15},
            {16, 17, 18},
        ],
        [
            {19, 20, 21},
            {22, 23, 24},
        ],
    ),
]


def extract_data_from_iterable(iterable):
    """Принимает в качестве аргумента итерируемый объект с произвольным количеством уровней вложенности, и возвращает список всех неитерируемых объектов, собранных со всех уровней вложенности."""
    result = []
    
    for elem in iterable:
        if type(elem) in (list, tuple, set):
            result.extend(extract_data_from_iterable(elem))
        else:
            result.append(elem)
    
    return result


# >>> extract_data_from_iterable(data1)
# [1, 2, 3, 4, 5, 6]
# >>>
# >>> extract_data_from_iterable(data2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# >>>
# >>> extract_data_from_iterable(data3)
# [1, 2, 3, 4, 5, 6, 8, 9, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24, 22, 23]

