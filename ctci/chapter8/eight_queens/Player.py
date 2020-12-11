class Player:
    def __init__(self):
        self._pieces = set()

    def add_piece(self, piece):
        self._pieces.add(piece)

    def remove_piece(self, piece):
        self._pieces.remove(piece)

    def get_piece_points(self):
        piece_points = {piece.get_point() for piece in self._pieces}
        return piece_points

    def get_all_attack_points(self):
        all_attack_points = set()
        for piece in self._pieces:
            all_attack_points = all_attack_points | piece.get_attack_points()
        return all_attack_points
