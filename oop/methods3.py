class Socket:
    cnt = 0
    
    def __init__(self):
        self.id = self.cnt
        self.__class__.cnt += 1
    
    def plug_in(self):
        print(f'розетка {self.id} включена')
        
    def plug_out(self):
        print(f'розетка {self.id} выключена')


hall1 = Socket()
hall2 = Socket()
liv_room1 = Socket()
liv_room2 = Socket()
liv_room3 = Socket()
kitchen1 = Socket()
kitchen2 = Socket()

# >>> Socket.cnt
# 7

def all_turn_on():
    for soc in (hall1, hall2, liv_room1, liv_room2, liv_room3, kitchen1, kitchen2):
        soc.plug_in()


def all_turn_off():
    for soc in (hall1, hall2, liv_room1, liv_room2, liv_room3, kitchen1, kitchen2):
        soc.plug_out()


# >>> all_turn_on()
# розетка 0 включена
# розетка 1 включена
# розетка 2 включена
# розетка 3 включена
# розетка 4 включена
# розетка 5 включена
# розетка 6 включена

