class Hero:
    def __init__(self, name, lvl, health, strength):
        self.Heroname = name
        self.Herolvl = lvl
        self.Herohealth = health
        self.Herostrength = strength
    def greet(self):
        print(f'|{self.Heroname}|  мои уровень = {self.Herolvl}|')
    def attack(self):
        print(f'{self.Heroname} наносит удар, уменьшает силу героя на 1')
    def rest(self):
        print(f'{self.Heroname} отдыхает 10 мин, уеличевает здоровьу героя на 1  ')

S1mple = Hero('S1mple', 15, 100, 1000)
Donk = Hero('Donk', 12, 90, 999)

print(f' Name = {S1mple.Heroname}, Lvl = {S1mple.Herolvl}, Health = {S1mple.Herohealth}, Strength = {S1mple.Herostrength}')
print(f'Name = {Donk.Heroname}, Lvl = {Donk.Herolvl}, Health = {Donk.Herohealth}, Strenght = {Donk.Herostrength}')
