class Box:
    def __init__(self):
        self.items = []
    
    def put_in(self, item):
        self.items.append(item)
        print(f'{item!r} помещён в коробку')
    
    def get_out(self, item):
        try:
            self.items.remove(item)
        except ValueError:
            print(f'{item} отсутствует в коробке')
        else:
            print(f'{item} убран из коробки')


box1 = Box()
box2 = Box()

for t in (13, 'vv', '!', -1, .5, 2.71):
    box2.put_in(t)
    # эквивалентно Box.put_in(box2, t)

