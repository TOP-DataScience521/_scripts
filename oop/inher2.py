class Proteus:
    @staticmethod
    def move():
        print('движение')
    
    @staticmethod
    def eat():
        print('питание')
    
    @staticmethod
    def reproduce():
        print('размножение')


class Fish(Proteus):
    @staticmethod
    def breath():
        print('дыхание')


class Reptile(Fish):
    @staticmethod
    def hide():
        print('скрытность')


class Bird(Reptile):
    @staticmethod
    def fly():
        print('полёт')


class Mammal(Reptile):
    @staticmethod
    def care():
        print('забота')


class Human(Mammal):
    @staticmethod
    def speak():
        print('речь')


from pprint import pp

ivan = Human()
kesha = Bird()

# >>> ivan
# <__main__.Human object at 0x0000021E8D244D70>
# >>>
# >>> ivan.__class__
# <class '__main__.Human'>
# >>>
# >>> pp(ivan.__class__.__mro__)
# (<class '__main__.Human'>,
#  <class '__main__.Mammal'>,
#  <class '__main__.Reptile'>,
#  <class '__main__.Fish'>,
#  <class '__main__.Proteus'>,
#  <class 'object'>)
# >>>
# >>>
# >>> kesha
# <__main__.Bird object at 0x0000021E8D244DA0>
# >>>
# >>> kesha.__class__
# <class '__main__.Bird'>
# >>>
# >>> pp(kesha.__class__.__mro__)
# (<class '__main__.Bird'>,
#  <class '__main__.Reptile'>,
#  <class '__main__.Fish'>,
#  <class '__main__.Proteus'>,
#  <class 'object'>)

# списки атрибутов, доступных при полностью расширенных областях видимости
# >>> pp(dir(ivan))
# [...,
#  'breath',
#  'care',
#  'eat',
#  'hide',
#  'move',
#  'reproduce',
#  'speak']
# >>>
# >>> pp(dir(kesha))
# [...,
#  'breath',
#  'eat',
#  'fly',
#  'hide',
#  'move',
#  'reproduce']

