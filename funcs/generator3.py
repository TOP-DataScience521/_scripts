def inf_counter(start, step=1):
    while True:
        yield start
        start += step


words = ('and', 'the', 'angle', 'cosine', 'word')
keys = ['A', 'D', 'A', 'G']

# >>> for elem in zip(words, keys):
# ...     print(elem)
# ...
# ('and', 'A')
# ('the', 'D')
# ('angle', 'A')
# ('cosine', 'G')
# >>>
# >>> for elem in zip(inf_counter(1), words, keys):
# ...     print(elem)
# ...
# (1, 'and', 'A')
# (2, 'the', 'D')
# (3, 'angle', 'A')
# (4, 'cosine', 'G')


# >>> for elem in zip(inf_counter(-1, -1), words):
# ...     print(elem)
# ...
# (-1, 'and')
# (-2, 'the')
# (-3, 'angle')
# (-4, 'cosine')
# (-5, 'word')

