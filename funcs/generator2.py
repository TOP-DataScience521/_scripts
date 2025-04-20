# l1 = [1, 2, 3, 4]
# l2 = [1, 1, 2, 2, 3, 3, 4, 4]


def element_doubler(iterable):
    for elem in iterable:
        yield elem
        yield elem


l1 = [4, 9, 2, 6]
l2 = list(element_doubler(l1))

# >>> l1
# [4, 9, 2, 6]
# >>> l2
# [4, 4, 9, 9, 2, 2, 6, 6]

