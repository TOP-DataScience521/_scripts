from datetime import date, timedelta as td


class Product:
    def __init__(
            self,
            name,
            produced,
            days_to_expire
    ):
        self.name = name
        self.produced = produced
        self.expired = produced + td(days=days_to_expire)
    
    def check(self):
        return date.today() < self.expired


class Fridge(list):
    def __init__(self, iterable):
        for elem in iterable:
            if type(elem) is Product:
                self.append(elem)
            else:
                raise TypeError
    
    def clear_expired(self):
        indexes = []
        for i, prod in enumerate(self):
            if not prod.check():
                indexes.append(i)
        for i in indexes:
            self.pop(i)



