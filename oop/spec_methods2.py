class Color:
    def __init__(self, color_html_hex_code, color_name=''):
        self.hex = color_html_hex_code
        self.name = color_name
    
    # self == other  -->  self.__eq__(other)
    def __eq__(self, other):
        if type(other) is self.__class__:
            return int(self.hex, 16) == int(other.hex, 16)
        elif type(other) is str:
            return int(self.hex, 16) == int(other, 16)
        else:
            raise TypeError
    
    # red < green  -->  red.__lt__(green)
    def __lt__(left_operand, right_operand):
        # print('вызван метод __lt__ от экземпляра', left_operand)
        if type(right_operand) is left_operand.__class__:
            return int(left_operand.hex, 16) < int(right_operand.hex, 16)
        elif type(right_operand) is str:
            return int(left_operand.hex, 16) < int(right_operand, 16)
        else:
            raise TypeError
    
    def __hash__(self):
        return int(self.hex, 16)


red = Color('ff0000', 'красный')
green = Color('00ff00', 'зелёный')

# >>> red < green
# False
# >>>
# >>> red.__lt__(green)
# False
# >>>
# >>> green < red
# True
# >>>
# >>> green.__lt__(red)
# True


red2 = Color('FF0000', 'red')

# >>> red == red2
# True
# >>>
# >>> {red: 'abc', green: 'def'}
# {<__main__.Color object at 0x00000196496C5190>: 'abc', <__main__.Color object at 0x00000196496C51C0>: 'def'}
# >>>
# >>> {red: 'abc', red2: 'def'}
# {<__main__.Color object at 0x00000196496C5190>: 'def'}
# >>>
# >>> {red, green}
# {<__main__.Color object at 0x00000196496C5190>, <__main__.Color object at 0x00000196496C51C0>}
# >>>
# >>> {red, red2}
# {<__main__.Color object at 0x00000196496C5190>}

