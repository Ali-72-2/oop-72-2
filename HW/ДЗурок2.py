

class Hero:
    def __init__(self, name, health, lvl, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'привет! моё имя {self.name}')

    def attack(self):
        print(f'{self.name} атакует')
    def rest(self):
        self.health += 10
        print(f'{self.name} отдохнул, здоровье востоновлено до {self.health}')

class Warrior(Hero):
    ...
class Mage(Hero):
    ...
class Assasin(Hero):
    ...



