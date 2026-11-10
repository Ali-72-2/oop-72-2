class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        print(f'{self.name} готов к бою')

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        print(f'Маг {self.name} кастует заклинание! MP: {self.mp}')

class WarriorHero(MageHero):
    def action(self):
        print(f'Войн {self.name} рубит мечом! Уровень: {self.lvl} ')

class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance= balance
        self.__password = password
        self.bank_name = bank_name

    def login(self,password):
        if password == self.__password :
            print('password is true ')
    @property
    def full_info(self):
        return f'Герой: {self.hero.name}, Баланс: {self._balance} SOM'
    def get_bank_name(self):
        return self.bank_name
    def bonus_for_level(self):
        return self.hero.lvl * 10
    def __str__(self):
        return f'{self.hero.name} | Баланс: {self._balance} SOM'
    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            print("Нельзя сложить счета геровем разных классов")

    def __eq__(self, other):
        if type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl:
            return True
        else:
            return False

mage1 = MageHero("Merlin", 50, 100, 150)
mage2 = MageHero("Gandalf", 50, 120, 200)
warrior = WarriorHero("Conan", 50, 200, 50)


mage1.action()
warrior.action()


# 6. Создание банковских счетов
acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "5678", "Simba")
acc3 = BankAccount(warrior, 4000, "9999", "Simba")


print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("Вход в аккаунт:", acc1.login("1234"))

print("Полная информация:", acc1.full_info)

print("\n=== Проверка __add__ ===")

print("Сумма счетов двух магов:", acc1 + acc2)

try:
    print("Сумма мага и воина:", acc1 + acc3)
except TypeError as error:
    print("Ошибка:", error)

print("\n=== Проверка __eq__ ===")

print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)
