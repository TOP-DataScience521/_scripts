def line_len(x1, y1, x2, y2, /):
    """Возвращает евклидово расстояние между двумя точками на плоскости."""
    return ((x2 - x1)**2 + (y2 - y1)**2)**.5


# >>> line_len(0, 0, 4, 0)
# 4.0
# >>> line_len(1, 1, 4, 5)
# 5.0
# >>>
# >>> line_len(x1=5, x2=1, y1=3, y2=3)
# TypeError: line_len() got some positional-only arguments passed as keyword arguments: 'x1, y1, x2, y2'
# >>>
# >>> line_len(x1=5, y1=3, x2=1, y2=3)
# TypeError: line_len() got some positional-only arguments passed as keyword arguments: 'x1, y1, x2, y2'

