import string
import random

class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password
        self._balance = balance

    def get_balance(self):
        return self._balance
    def __radnom_pass(self):
        chart = string.ascii_letters + string.digits
        password = ''.join(random.choise(chart for i in range(6)))
        return password
    def reset_pass(self, old_pass):
        if old_pass == self.__password:
            self.__password = self.__random_pass()
        else:
            'не верный старый пороль'
            self._balance = self._balance - self.__password
    # def get_pasword(self):
    #     return self.__password

# ardager = BankAccount('ardager', 'Def2638', 1000)
#
# print(ardager._balance)
# print(ardager.reset_pass('Def2638'))
# print(ardager._BankAccount__password)

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('gaf gaf')
    def move(self):
        print('step')
gufi = Dog()












