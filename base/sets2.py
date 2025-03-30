mammals = {'тигр', 'верблюд', 'баран', 'кит', 'морж'}
aquatic = {'осьминог', 'кальмар', 'краб', 'кит', 'морж'}

aquatic_mammals = {'кит', 'морж'}
reptiles = {'черепаха', 'змея', 'ящерица', 'крокодил'}


# >>> mammals | aquatic
# {'верблюд', 'баран', 'кит', 'краб', 'кальмар', 'осьминог', 'тигр', 'морж'}
# >>>
# >>> mammals & aquatic
# {'морж', 'кит'}
# >>>
# >>> mammals & reptiles
# set()
# >>>
# >>> mammals - aquatic
# {'верблюд', 'баран', 'тигр'}
# >>>
# >>> aquatic - mammals
# {'осьминог', 'краб', 'кальмар'}
# >>>
# >>> mammals ^ aquatic
# {'верблюд', 'осьминог', 'баран', 'тигр', 'краб', 'кальмар'}
# >>>
# >>> (mammals | aquatic) - (mammals & aquatic)
# {'верблюд', 'баран', 'краб', 'кальмар', 'осьминог', 'тигр'}


# >>> aquatic_mammals < mammals
# True
# >>> aquatic_mammals < aquatic
# True
# >>>
# >>> aquatic_mammals > aquatic
# False
# >>> aquatic > aquatic_mammals
# True
# >>>
# >>> {1, 2, 3} < {1, 2, 3}
# False
# >>> {1, 2, 3} <= {1, 2, 3}
# True


# >>> bool(mammals & aquatic)
# True
# >>> bool(mammals & reptiles)
# False
# >>>
# >>> mammals.isdisjoint(aquatic)
# False
# >>> mammals.isdisjoint(reptiles)
# True

