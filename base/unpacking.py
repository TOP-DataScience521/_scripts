numbers = [4, 9, -2, 7]

# >>> print(numbers)
# [4, 9, -2, 7]
# >>>
# >>> print(numbers, sep='\n')
# [4, 9, -2, 7]
# >>>
# >>> print(*numbers, sep='\n')
# 4
# 9
# -2
# 7


# >>> n1, n2, n3, n4 = numbers
# >>> n1
# 4
# >>> n2
# 9
# >>> n3
# -2
# >>> n4
# 7
# >>>
# >>> n1, n2, n3 = numbers
# ValueError: too many values to unpack (expected 3)
# >>>
# >>> n1, n2, n3, n4, n5 = numbers
# ValueError: not enough values to unpack (expected 5, got 4)


# >>> left, right = (0, 25)
# >>> left
# 0
# >>> right
# 25
# >>>
# >>> left, right = 100, 150
# >>> left
# 100
# >>> right
# 150


# >>> nums = 1, 2, 3
# >>> nums
# (1, 2, 3)
# >>>
# >>> type(nums)
# <class 'tuple'>
# >>>
# >>> left, right
# (100, 150)
# >>>
# >>> left, right = right, left
# >>> left
# 150
# >>> right
# 100


alphabet = ['Аа', 'Бб', 'Вв', 'Гг']

for elem in alphabet:
    print(repr(elem))

# 'Аа'
# 'Бб'
# 'Вв'
# 'Гг'

for u_case, l_case in alphabet:
    print(repr(u_case), repr(l_case), sep='\t')

# 'А'     'а'
# 'Б'     'б'
# 'В'     'в'
# 'Г'     'г'

alphabet = ['1Аа', '2Бб', '3Вв', '4Гг']

for num, u_case, l_case in alphabet:
    print(int(num), repr(u_case), repr(l_case), sep='\t')

# 1       'А'     'а'
# 2       'Б'     'б'
# 3       'В'     'в'
# 4       'Г'     'г'

