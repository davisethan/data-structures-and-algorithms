from abc import ABC
from Board import Board
from Piece import Queen
from Player import Player
from Point import Point

class EightQueensStategy(ABC):
    def eight_queens_strategy(self):
        pass

class RecursiveEightQueensStrategy(EightQueensStategy):
    def __init__(self, player):
        self._player = player
        self._seen_eight_queens = set()

    def eight_queens_strategy(self):
        self.eight_queens_strategy_step()
        return self.seen_eight_queens

    def eight_queens_strategy_step(self):
        if 0 < len(self._seen_eight_queens):
            return

        if 8 == len(self._player.get_piece_points()):
            seen_eight_queens.add(self._player.get_piece_points())
            return
        
        for row in range(Board.ROWS):
            for column in range(Board.COLUMNS):
                point = Point(row, column)
                
                if point in self._player.get_piece_points() or point in self._player.get_all_attack_points():
                    continue

                queen = Queen(Point(row, column))
                self._player.add_piece(queen)
                self.eight_queens_strategy_step()
                self._player.remove_piece(queen)
