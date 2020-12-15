from abc import ABC
from collections import deque

class Bank:
    def __init__(self):
        self._COST = 25
        self._coins = deque()

    def get_coins(self):
        return self._coins

    def has_enough(self):
        summed = 0
        for coin in self._coins:
            summed += coin.CENTS
        return self._COST <= summed

    def take_enough(self):
        summed = 0
        while self._COST > summed:
            coin = self._coins.popleft()
            summed += coin.CENTS

    def add_coins(self, coins):
        for coin in coins:
            self._coins.append(coin)

    def remove_coins(self):
        copy = deque(self._coins)
        self._coins = deque()
        return copy

class Coin(ABC):
    pass

class Quarter(Coin):
    CENTS = 25

class Dime(Coin):
    CENTS = 10

class Nickel(Coin):
    CENTS = 5

class Penny(Coin):
    CENTS = 1
