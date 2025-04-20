def gcd(num1, num2):
    """Возвращает наибольший общий делитель (НОД) для чисел num1 и num2."""
    rem = num1 % num2
    if rem:
    # то же самое
    # if rem != 0:
        return gcd(num2, rem)
    else:
        return num2


# >>> gcd(12, 6)
# 6
# >>>
# >>> gcd(15, 12)
# 3
# >>>
# >>> gcd(19, 7)
# 1

