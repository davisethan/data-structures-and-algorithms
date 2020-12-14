from abc import ABC

class Coin(ABC):
    CENTS: int

class Quarter(Coin):
    CENTS: int = 25

class Dime(Coin):
    CENTS: int = 10

class Nickel(Coin):
    CENTS: int = 5

class Penny(Coin):
    CENTS: int = 1
