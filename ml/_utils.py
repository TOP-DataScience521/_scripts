from itertools import zip_longest


def concatenate_lines(*columns, column_width: int = 40, separator: str = ' | '):
    columns_lines = [col.split('\n') for col in columns]
    paragraph = []
    for lines in zip_longest(*columns_lines, fillvalue=''):
        paragraph.append(separator.join([
            f'{line:<{column_width}}' 
            for line in lines
        ]))
    return '\n'.join(paragraph)


Point = tuple[float, float]

def euclid_dist(point1: Point, point2: Point):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

