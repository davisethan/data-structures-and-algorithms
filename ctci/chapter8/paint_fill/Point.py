
class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y
