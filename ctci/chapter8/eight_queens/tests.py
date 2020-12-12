import unittest
from Board import Board
from Game import Game
from Piece import Queen
from Player import Player
from Point import Point

class TestHash(unittest.TestCase):
    def test_point_hash(self):
        lot = set()
        
        for row in range(Board.ROWS):
            for column in range(Board.COLUMNS):
                hashable = f"{row}{column}"
                lot.add(hash(hashable))
        
        self.assertEqual(Board.ROWS * Board.COLUMNS, len(lot))

    def test_piece_hash(self):
        lot = set()

        for row in range(Board.ROWS):
            for column in range(Board.COLUMNS):
                hashable = f"Q{row}{column}"
                lot.add(hash(hashable))

        self.assertEqual(Board.ROWS * Board.COLUMNS, len(lot))

class TestQueen(unittest.TestCase):
    def test_queen_upper_vertical_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_upper_vertical_attack_points = {Point(1, 4), Point(0, 4)}

        actual_upper_vertical_attack_points = queen._get_upper_vertical_attack_points()

        self.assertEqual(expected_upper_vertical_attack_points, actual_upper_vertical_attack_points)

    def test_queen_right_horizonal_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_right_horizontal_attack_points = {Point(2, 5), Point(2, 6), Point(2, 7)}

        actual_right_horizontal_attack_points = queen._get_right_horizontal_attack_points()

        self.assertEqual(expected_right_horizontal_attack_points, actual_right_horizontal_attack_points)

    def test_queen_lower_vertical_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_lower_vertical_attack_points = {Point(3, 4), Point(4, 4), Point(5, 4), Point(6, 4), Point(7, 4)}

        actual_lower_vertical_attack_points = queen._get_lower_vertical_attack_points()

        self.assertEqual(expected_lower_vertical_attack_points, actual_lower_vertical_attack_points)

    def test_queen_left_horizonal_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_left_horizontal_attack_points = {Point(2, 3), Point(2, 2), Point(2, 1), Point(2, 0)}

        actual_left_horizontal_attack_points = queen._get_left_horizontal_attack_points()

        self.assertEqual(expected_left_horizontal_attack_points, actual_left_horizontal_attack_points)

    def test_queen_upper_right_diagonal_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_upper_right_diagonal_attack_points = {Point(1, 5), Point(0, 6)}

        actual_upper_right_diagonal_attack_points = queen._get_upper_right_diagonal_attack_points()

        self.assertEqual(expected_upper_right_diagonal_attack_points, actual_upper_right_diagonal_attack_points)

    def test_queen_lower_right_diagonal_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_lower_right_diagonal_attack_points = {Point(3, 5), Point(4, 6), Point(5, 7)}

        actual_lower_right_diagonal_attack_points = queen._get_lower_right_diagonal_attack_points()

        self.assertEqual(expected_lower_right_diagonal_attack_points, actual_lower_right_diagonal_attack_points)

    def test_queen_lower_left_diagonal_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_lower_left_diagonal_attack_points = {Point(3, 3), Point(4, 2), Point(5, 1), Point(6, 0)}

        actual_lower_left_diagonal_attack_points = queen._get_lower_left_diagonal_attack_points()

        self.assertEqual(expected_lower_left_diagonal_attack_points, actual_lower_left_diagonal_attack_points)

    def test_queen_upper_left_diagonal_attack_points_2_4(self):
        queen = Queen(Point(2, 4))
        expected_upper_left_diagonal_attack_points = {Point(1, 3), Point(0, 2)}

        actual_upper_left_diagonal_attack_points = queen._get_upper_left_diagonal_attack_points()

        self.assertEqual(expected_upper_left_diagonal_attack_points, actual_upper_left_diagonal_attack_points)

class TestPlayer(unittest.TestCase):
    def test_player_get_piece_points(self):
        expected_player_piece_points = {Point(0, 0), Point(1, 2), Point(2, 4)}
        player = Player()
        for point in expected_player_piece_points:
            player.add_piece(Queen(point))

        actual_player_piece_points = player.get_piece_points()

        self.assertEqual(expected_player_piece_points, actual_player_piece_points)

    def test_player_get_all_attack_points(self):
        expected_player_all_attack_points = set()
        queens = {Queen(Point(0, 0)), Queen(Point(7, 7))}
        player = Player()
        for queen in queens:
            player.add_piece(queen)
            expected_player_all_attack_points = expected_player_all_attack_points | queen.get_attack_points()

        actual_player_all_attack_points = player.get_all_attack_points()

        self.assertEqual(expected_player_all_attack_points, actual_player_all_attack_points)

class TestEightQueensStrategy(unittest.TestCase):
    def test_recursive_eight_queens_strategy(self):
        game = Game()
        eight_queens_solution = game.initial_placement()
        print(eight_queens_solution)

if __name__ == "__main__":
    unittest.main()
