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

