from abc import ABC
from Board import Board
from Point import Point

class Piece(ABC):
    def __init__(self, point):
        self._point = point

    def get_point(self):
        return self._point

    def get_attack_points(self):
        pass

class Queen(Piece):
    def __init__(self, point):
        super().__init__(point)

    def __hash__(self):
        return hash(f"Q{self._point}")

    def get_attack_points(self):
        attack_points = set()
        attack_points = attack_points | self._get_upper_vertical_attack_points()
        attack_points = attack_points | self._get_right_horizontal_attack_points()
        attack_points = attack_points | self._get_lower_vertical_attack_points()
        attack_points = attack_points | self._get_left_horizontal_attack_points()
        attack_points = attack_points | self._get_upper_right_diagonal_attack_points()
        attack_points = attack_points | self._get_lower_right_diagonal_attack_points()
        attack_points = attack_points | self._get_lower_left_diagonal_attack_points()
        attack_points = attack_points | self._get_upper_left_diagonal_attack_points()
        return attack_points

    def _get_upper_vertical_attack_points(self):
        upper_vertical_attack_points = {Point(self._point.get_x() - row, self._point.get_y()) for row in range(1, Board.ROWS) if 0 <= self._point.get_x() - row}
        return upper_vertical_attack_points

    def _get_right_horizontal_attack_points(self):
        right_horizontal_attack_points = {Point(self._point.get_x(), self._point.get_y() + column) for column in range(1, Board.COLUMNS) if Board.COLUMNS > self._point.get_y() + column}
        return right_horizontal_attack_points

    def _get_lower_vertical_attack_points(self):
        lower_vertical_attack_points = {Point(self._point.get_x() + row, self._point.get_y()) for row in range(1, Board.ROWS) if Board.ROWS > self._point.get_x() + row}
        return lower_vertical_attack_points

    def _get_left_horizontal_attack_points(self):
        left_horizontal_attack_points = {Point(self._point.get_x(), self._point.get_y() - column) for column in range(1, Board.COLUMNS) if 0 <= self._point.get_y() - column}
        return left_horizontal_attack_points

    def _get_upper_right_diagonal_attack_points(self):
        upper_right_diagonal_attack_points = {Point(self._point.get_x() - index, self._point.get_y() + index) for index in range(1, Board.ROWS) if 0 <= self._point.get_x() - index and Board.COLUMNS > self._point.get_y() + index}
        return upper_right_diagonal_attack_points

    def _get_lower_right_diagonal_attack_points(self):
        lower_right_diagonal_attack_points = {Point(self._point.get_x() + index, self._point.get_y() + index) for index in range(1, Board.ROWS) if Board.ROWS > self._point.get_x() + index and Board.COLUMNS > self._point.get_y() + index}
        return lower_right_diagonal_attack_points

    def _get_lower_left_diagonal_attack_points(self):
        lower_left_diagonal_attack_points = {Point(self._point.get_x() + index, self._point.get_y() - index) for index in range(1, Board.ROWS) if Board.ROWS > self._point.get_x() + index and 0 <= self._point.get_y() - index}
        return lower_left_diagonal_attack_points
    
    def _get_upper_left_diagonal_attack_points(self):
        upper_left_diagonal_attack_points = {Point(self._point.get_x() - index, self._point.get_y() - index) for index in range(1, Board.ROWS) if 0 <= self._point.get_x() - index and 0 <= self._point.get_y() - index}
        return upper_left_diagonal_attack_points
