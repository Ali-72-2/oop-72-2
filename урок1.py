class Hero:
    def __init__(self, name, lvl,  hp):
        self.hero_lvl = lvl
        self.hero_hp = hp

    def action(self):
        print(f'{self.hero_name} base action')
kirito = Hero('Kirito', 100, 1000)
asuna = Hero('Asuna', 101, 1010)
# print(kirito.hero_lvl)
# print(kirito.hero_hp)
print(type())