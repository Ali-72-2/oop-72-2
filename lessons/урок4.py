"""Магчиеские методы"""
# __init__
class Test:
    def __init__(self, value):
        self.value = value
    # print()
    def __str__(self):
        return self.value

    def __add__(self, other):
        return f'{self.value + other.value}'
t_1 = Test(123)
t_2 = Test(321)
value_t = t_1 + t_2
print(value_t)

class Video:
    def __init__(self, content, titel, descriptions):
        self.content = content
        self.titel = titel
        self.descriptions = descriptions
        self.view_count = 0

    def __call__(self, *args, **kwargs):
        self.view_count += 1
        # print(self.view_count)
video1 = Video("Test", "Titel", "descriptions")


# test_obj = Test('Test Text')
# my_str = 'My text'

class BankAccount:

    def __init__(self, login, first_name, last_name, balance =100, bonus)
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.bonus = bonus

    @staticmethod
    def calculate_deposit():
        return 123
    @classmethod
    def get_bank_name(cls):
     print(f'{cls.bamk_name}')
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    @property
    def total_balance(self):
        print(f'{self.balance + self.bonus}')
        

ardager = BankAccount("Ardager.kg", "aradger", "kartanbekov")
arzy = BankAccount("Arzy.kg", "arzybek", "adyramkhmanov")
# ardager.calculate_deposit()
print(arzy.full_name)