from EightQueensStrategy import RecursiveEightQueensStrategy
from Player import Player

class Game:
    def __init__(self):
        self._player = Player()
        self._recursive_eight_queens_strategy = RecursiveEightQueensStrategy(self._player)

    def initial_placement(self):
        return self._recursive_eight_queens_strategy.eight_queens_strategy()
