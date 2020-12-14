from abc import ABC
from Coin import Coin, Quarter, Dime, Nickel, Penny

class CreateCentsStrategy(ABC):
    def create_cents(self, cents: int):
        pass

class RecursiveCreateCentsStrategy(CreateCentsStrategy):
    def __init__(self):
        self._seen_coins: set[Coin] = set()
        self._coins: tuple[Coin] = tuple()

    def create_cents(self, cents: int) -> set:
        self.create_cents_step(cents)
        return self._seen_coins

    def create_cents_step(self, cents: int) -> None:
        if 0 > cents:
            return
        elif 0 == cents:
            self._seen_coins.add(self._coins)
        else:
            coins: tuple[Coin] = (Quarter, Dime, Nickel, Penny)
            for coin in coins:
                self.create_cents_with_coin(cents, coin)

    def create_cents_with_coin(self, cents: int, coin: Coin) -> None:
        self._coins += (coin,)
        self.create_cents(cents - coin.CENTS)
        self._coins = self._coins[:-1]
