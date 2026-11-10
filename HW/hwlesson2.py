
import random
class Hero:
    def __init__(self, name, health, lvl, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'привет! моё имя {self.name}')

    def attack(self):
        print(f'{self.name} атакует c силой {self.strength}!')

    def rest(self):
        self.health += 10
        print(f'{self.name} отдохнул, здоровье востоновлено до {self.health}')

class Warrior(Hero):
    def __init__(self, name, health, lvl, strength, stamina):
        super().__init__(name, lvl, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f'{self.name} атакует мечом! ')



class Mage(Hero):
    def __init__(self, name, health, lvl, strength, mana):
        super().__init__(name, lvl, health, strength)

        self.mana = mana

    def attack(self):
        print(f'{self.name} кастует заклинание! ')



class Assasin(Hero):
    def __init__(self, name, health, lvl, strength, stealth):
        super().__init__(name, lvl, health, strength)

        self.stealth = stealth

    def attack(self):
        print(f'{self.name} атакует из под тишка! ')

warrior = Warrior('воин', 250, 100, 90, 110)
mage = Mage('Маг', 100, 120, 50,200)
assasin = Assasin('Ассасин', 200, 100, 150, 500)

print(" наши герои = ")

warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assasin.greet()
assasin.attack()
assasin.rest()

print("игра ")
heroes = {
    "Warrior": warrior,
    "Mage": mage,
    "Assasin": assasin,
}

user_choise = input("выьерете героя (Warrior, Mage, Assasin): )").strip().capitalize()
if user_choise not in heroes:
    print("Такого героя нету! Побробуйте снова. ")
else:
    enemy_choise = random.choice(list(heroes.keys()))

    print(f'Вы выбрали {user_choise}!')
    print(f'Противник {enemy_choise}!')

    winning_combinations = {
            "Warrior": "Assassin",
            "Assassin": "Mage",
            "Mage": "Warrior"
    }
    if user_choise == enemy_choise:
        print("Ничья!")
    elif winning_combinations[user_choise] == enemy_choise:
        print(f"{user_choise} победил!")
    else:
        print(f'{enemy_choise} победил!')
