from random import randrange as rr


MESSAGES = {
    'повышение уровня 1': 'Герой стал сильнее!',
    'повышение уровня 2': 'Герой стал значительно сильнее!',
    'победа над врагом': '...',
    'смерть': 'Герой погиб...',
    # '': '',
}


class Hero:
    def __init__(self):
        self.lvl = 1
        self.hp_max = 100
        self.hp = 100
        self.attack = 2
        self.defense = 1
    
    def lvl_up(self):
        self.lvl += 1
        self.hp_max += 10
        self.hp = self.hp_max
        self.attack += 1
        if self.lvl % 2:
            self.defense += 1
        self.lvl_up_msg()
    
    def get_punched(self, enemy_attack):
        self.hp -= (enemy_attack - self.defense) * 10
    
    @staticmethod
    def lvl_up_msg():
        messages = [
            v
            for k, v in MESSAGES.items()
            if k.startswith('повышение уровня')
        ]
        print(messages[rr(len(messages))])
    
    @staticmethod
    def death_msg():
        print(MESSAGES['смерть'])


konan = Hero()

# >>> konan.lvl
# 1
# >>> konan.lvl_up()
# Герой стал сильнее!
# >>> konan.lvl
# 2
# >>>
# >>> konan.lvl_up()
# Герой стал сильнее!
# >>> konan.lvl
# 3
# >>>
# >>> konan.lvl_up()
# Герой стал значительно сильнее!
# >>> konan.lvl
# 4
# >>>
# >>> konan.death_msg()
# Герой погиб...

