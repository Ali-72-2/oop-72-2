
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
    def __init__(self, name, health, lvl, strength):
        super().__init__(name, lvl, health, strength)

        self.stamina = stamina

    def attack(self):
        print(f'{self.name} атакует мечом! ')



class Mage(Hero):
    def __init__(self, name, health, lvl, strength):
        super().__init__(name, lvl, health, strength)

        self.mana = mana

    def attack(self):
        print(f'{self.name} кастует заклинание! ')



class Assasin(Hero):
    def __init__(self, name, health, lvl, strength):
        super().__init__(name, lvl, health, strength)

        self.stealth = stealth

    def attack(self):
        print(f'{self.name} атакует из под тишка! ')


print(" наши герои = ")

Warrior.greet()
Warrior.attack()
Warrior.rest()

Mage.greet()
Mage.attack()
Mage.rest()

Assasin.greet()
Assasin.attack()
Assasin.rest()

print("игра ")
heroes = {
    "Warrior": Warrior,
    "Mage": Mage,
    "Assasin": Assasin,
}

user_choise = input("выьерете героя (Warrior, Mage, Assasin): )").strip().capitalize()
if user_choise in heroes:
    print("Такого героя нету! Побробуйте снова. ")
else:
    enemy_choise = random.choise(list(heroes.keys()))

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
