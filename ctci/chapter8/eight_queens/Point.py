def point(x, y):
    return f"{x}{y}"

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f"{self._x}{self._y}"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return str(self) == str(other)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
