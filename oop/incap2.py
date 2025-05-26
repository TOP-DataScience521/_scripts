from datetime import datetime as dt
from pprint import pp


class BancAccount:
    _overdraft = 50000
    
    def __init__(self):
        self.__balance = 0
        self._history = {}
    
    # классический "геттер"
    def get_balance(self):
        self.__log('ЗАПРОС БАЛАНСА')
        return self.__balance
    
    # классический "сеттер"
    def deposit(self, amount):
        self.__log('ПОПОЛНЕНИЕ')
        self.__balance += amount
    
    # классический "сеттер"
    def withdraw(self, amount):
        new_balance = self.__balance - amount
        if abs(new_balance) < self._overdraft:
            self.__log('СНЯТИЕ')
            self.__balance = new_balance
        else:
            self.__log('ПРЕВЫШЕНИЕ ЛИМИТА')
            raise ValueError
    
    def __log(self, action):
        self._history[dt.now()] = action
    
    def __repr__(self):
        return f'{self.__balance} ₽'




