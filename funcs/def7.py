def perimeter(point1, point2, point3, *points):
    """Вычисляет и возвращает периметр многоугольника, заданного координатами вершин."""
    # print(f'{point1 = } {point2 = } {point3 = } {points = }')
    
    points = (point1, point2, point3, *points, point1)
    # print(f'{points = }')
    
    result = 0
    for i in range(len(points) - 1):
        # point1, point2 = points[i:i+2]
        # print(point1, point2, sep='\t')
        
        (x1, y1), (x2, y2) = points[i:i+2]
        # print(x1, y1, '\t', x2, y2)
        
        # result = result + ((x2 - x1)**2 + (y2 - y1)**2)**.5
        result += ((x2 - x1)**2 + (y2 - y1)**2)**.5
    
    return result


# >>> perimeter((0, 0), (4, 0))
# TypeError: perimeter() missing 1 required positional argument: 'point3'
# >>>
# >>> perimeter((0, 0), (4, 0), (2, 4))
# point1 = (0, 0) point2 = (4, 0) point3 = (2, 4) points = ()
# >>>
# >>> perimeter((0, 0), (4, 0), (4, 4), (0, 4))
# point1 = (0, 0) point2 = (4, 0) point3 = (4, 4) points = ((0, 4),)
# >>>
# >>> perimeter((0, 0), (4, 0), (5, 3), (3, 4), (-1, 3))
# point1 = (0, 0) point2 = (4, 0) point3 = (5, 3) points = ((3, 4), (-1, 3))


# >>> perimeter((0, 0), (4, 0), (5, 3), (3, 4), (-1, 3))
# 0 0      4 0
# 4 0      5 3
# 5 3      3 4
# 3 4      -1 3
# -1 3     0 0
# 16.683728923454208


# >>> perimeter((0, 0), (4, 0), (4, 4), (0, 4))
# 16.0

