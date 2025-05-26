class Square:
    def __init__(self, size):
        self.__size = size
        self.__area = size ** 2
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, new_size):
        self.__size = new_size
        self.__area = new_size ** 2
    
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, new_area):
        self.__size = new_area ** 0.5
        self.__area = new_area


sq1 = Square(5)

# >>> sq1.size
# 5
# >>> sq1.area
# 25
# >>>
# >>> sq1.size = 7
# >>> sq1.area
# 49
# >>>
# >>> sq1.area = 100
# >>> sq1.size
# 10.0

