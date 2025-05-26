class Person:
    def __init__(
            self,
            last_name,
            first_name,
            patr_name,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.patr_name = patr_name
    
    @property
    def full(self):
        return f'{self.last_name} {self.first_name} {self.patr_name}'
    
    @property
    def initials_first(self):
        return f'{self.first_name[0]}. {self.patr_name[0]}. {self.last_name}'
    
    @property
    def initials_last(self):
        return f'{self.last_name} {self.first_name[0]}. {self.patr_name[0]}.'
    
    @property
    def name(self):
        return f'{self.first_name} {self.patr_name}'
    
    @property
    def short_name(self):
        return f'{self.first_name}'

    def __repr__(self):
        return f'<Person: {self.short_name}>'

    def __str__(self):
        return self.full


liza = Person('Анисимова', 'Елизавета', 'Андреевна')

# >>> liza
# <Person: Елизавета>
# >>>
# >>> liza.full
# 'Анисимова Елизавета Андреевна'
# >>>
# >>> liza.initials_first
# 'Е. А. Анисимова'
# >>>
# >>> liza.initials_last
# 'Анисимова Е. А.'
# >>>
# >>> liza.name
# 'Елизавета Андреевна'
# >>>
# >>> liza.short_name
# 'Елизавета'

# >>> liza.last_name = 'Козлодуева'
# >>> liza.full
# 'Козлодуева Елизавета Андреевна'
# >>> liza.initials_last
# 'Козлодуева Е. А.'

