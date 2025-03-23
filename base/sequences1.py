text = 'строка для примера'

# >>> text[0]
# 'с'
# >>> text[1]
# 'т'

i = 10
# >>> text[i]
# ' '
# >>>
# >>> text[i+1]
# 'п'

# >>> text[1.0]
# TypeError: string indices must be integers, not 'float'
# >>>
# >>> i/2
# 5.0
# >>> text[i/2]
# TypeError: string indices must be integers, not 'float'
# >>>
# >>> i//2
# 5
# >>> text[i//2]
# 'а'

# >>> text[17]
# 'а'
# >>>
# >>> text[18]
# IndexError: string index out of range
# >>>
# >>> text[20]
# IndexError: string index out of range

# >>> text[len(text)-1]
# 'а'
# >>> text[len(text)-2]
# 'р'
# >>> text[len(text)-3]
# 'е'
# >>>
# >>> text[-1]
# 'а'
# >>> text[-2]
# 'р'
# >>> text[-3]
# 'е'

