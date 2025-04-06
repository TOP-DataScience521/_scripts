def name(form):
    if form == 'full':
        return 'Геннадий Дмитриевич Шаповаленко'
    elif form == 'initials':
        return 'Г. Д. Шаповаленко'
    elif form == 'name':
        return 'Геннадий'
    elif form == 'nick':
        return 'GennDALF'


# >>> name('name')
# 'Геннадий'
# >>>
# >>> name('nick')
# 'GennDALF'
# >>>
# >>> name('full')
# 'Геннадий Дмитриевич Шаповаленко'
# >>>
# >>> name('initials')
# 'Г. Д. Шаповаленко'

# >>> name('имя')
# >>>
# >>> name(56)
# >>>

