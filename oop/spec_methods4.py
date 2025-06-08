class Battery:
    def __init__(self, capacity):
        self.value = 0
        self.capacity = capacity
    
    # left_operand + right_operand  -->  left_operand.__add__(right_operand)
    def __add__(left_operand, right_operand):
        if right_operand.__class__ is left_operand.__class__:
            total = left_operand.value + right_operand.value
            if total > left_operand.capacity:
                left_operand.value = left_operand.capacity
                right_operand.value = total - left_operand.capacity
            else:
                left_operand.value = total
                right_operand.value = 0
        
        elif right_operand.__class__ is int:
            total = left_operand.value + right_operand
            if total > left_operand.capacity:
                left_operand.value = left_operand.capacity
            else:
                left_operand.value = total
        
        else:
            raise TypeError
        
        return left_operand
    
    def __bool__(self):
        return bool(self.value)
    
    def __repr__(self):
        return f'<Battery: {self.value}/{self.capacity}>'


krona = Battery(9)

# >>> krona
# <Battery: 0/9>
# >>>
# >>> krona.value
# 0
# >>> krona.capacity
# 9

# >>> krona + 2
# <Battery: 2/9>
# >>>
# >>> krona
# <Battery: 2/9>
# >>>
# >>>
# >>> krona + 5
# <Battery: 7/9>
# >>>
# >>> krona + 4
# <Battery: 9/9>
# >>>
# >>> krona + 123456
# <Battery: 9/9>


# >>> krona
# <Battery: 0/9>
# >>>
# >>> if krona:
# ...     print('заряжена')
# ... else:
# ...     print('не заряжена')
# ...
# не заряжена
# >>>
# >>> krona + 6
# <Battery: 6/9>
# >>>
# >>> if krona:
# ...     print('заряжена')
# ... else:
# ...     print('не заряжена')
# ...
# заряжена
# >>>
# >>> bool(krona)
# True

