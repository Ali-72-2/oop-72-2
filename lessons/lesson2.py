
#Родительский класс
class Hero:
    #конструктор класса
    def __init__(self, name, lvl,  hp):
        #Атрибуты экземпляра + ъj,mtrnf rkfccf
        self.name = name
        self.hero_lvl = lvl
        self.hero_hp = hp

    def action(self):
        print(f'{self.hero_name} base action')

# Дочерний класс
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def cast_spell(self):
        print(f"{self.name} cast fire bool")
kirito = Hero('Kirito', 111, 1111)
gendalf = MageHero("Gendalf", 100, 1000, 100)

#множественное наследевотильство
class Fly:
    def fly(self):
        print('Fly')
class  Swimm:
    def swimm(self):
        print('Swim')
class Animal(Swimm, Fly):
    pass
