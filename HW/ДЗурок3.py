
from abc import ABC, abstractmethod


class Hero:
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.__health = health
        self.strength = strength
    def greet(self):
        print(f'Привет! я {self.name}, мой уровень {self.lvl} ')
    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass
class Warrior(Hero):
    def attack(self):
        print(f'Войн аттакует мечом')
class Mage(Hero):
    def attack(self):
        print('Маг использует магию')
class Assassin(Hero):
    def attack(self):
        print('Ассасин аттакует из-под тишка')

warrior = Warrior("Артур", 250, 500, 200)
mage = Mage("Мерлин", 120, 200, 30)
assassin = Assassin("Тень", 150, 100, 150)

warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()
