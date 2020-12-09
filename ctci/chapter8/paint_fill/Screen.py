from Color import Color
from Point import Point

class Screen:
    def __init__(
        self,
        rows: int,
        columns: int,
        color: Color = Color(0, 0, 0)) -> None:
        self._rows = rows
        self._columns = columns
        self._screen = [[color for column in range(columns)] for row in range(rows)]

    def __str__(self) -> str:
        screen = "["
        for row in range(self._rows):
            screen += "["
            for column in range(self._columns):
                screen += f"{str(self._screen[row][column])},"
            screen = screen[:-1] + "]\n"
        screen = screen[:-1] + "]"
        return screen

    def get_rows(self) -> int:
        return self._rows

    def get_columns(self) -> int:
        return self._columns

    def get_color_at_point(self, point: Point) -> Color:
        return self._screen[point.get_x()][point.get_y()]

    def set_color_at_point(self, point: Point, color: Color) -> None:
        self._screen[point.get_x()][point.get_y()] = color
