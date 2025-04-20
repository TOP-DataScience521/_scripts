words = ('and', 'the', 'angle', 'cosine', 'word')

generator_obj = (len(word) for word in words)

# >>> generator_obj
# <generator object <genexpr> at 0x000001D223DCC520>
# >>>
# >>> for elem in generator_obj:
# ...     print(elem)
# ...
# 3
# 3
# 5
# 6
# 4


# >>> sum(len(w) for w in words)
# 21

