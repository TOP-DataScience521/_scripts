# >>> 10 if True else 20
# 10
# >>> 10 if False else 20
# 20


var = 10 if False else 20
# >>> var
# 20

var = 10 if False else (20 if True else 40)
# >>> var
# 20

var = 10 if False else (20 if False else 40)
# >>> var
# 40


# >>> print(10 if False else 20, 30 if True else 40)
# 20 30

