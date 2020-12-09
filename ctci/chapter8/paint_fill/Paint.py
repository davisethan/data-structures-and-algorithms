
class Point:
    def __init__(self, cartesian_x: int, cartesian_y: int) -> None:
        self._cartesian_x = cartesian_x
        self._cartesian_y = cartesian_y

    def __str__(self):
        return f"({self._cartesian_x}, {self._cartesian_y})"

    def get_cartesian_x(self) -> int:
        return self._cartesian_x

    def get_cartesian_y(self) -> int:
        return self._cartesian_y

class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    def __str__(self) -> str:
        return str((self._red, self._green, self._blue))

class Screen:
    def __init__(self, rows: int, columns: int, color: Color = Color(0, 0, 0)) -> None:
        self._rows = rows
        self._columns = columns
        self._screen = [[color for column in range(columns)] for row in range(rows)]

    def __str__(self) -> str:
        screen = [[str(self._screen[row][column]) for column in range(self._columns)] for row in range(self._rows)]
        screen = str(screen)
        return screen

    def get_rows(self) -> int:
        return self._rows

    def get_columns(self) -> int:
        return self._columns

    def get_color_at_point(self, point: Point) -> Color:
        return self._screen[point.get_cartesian_x()][point.get_cartesian_y()]

    def set_color_at_point(self, point: Point, color: Color) -> None:
        self._screen[point.get_cartesian_x()][point.get_cartesian_y()] = color

    def paint_fill(self, point: Point, color: Color) -> None:
        paint_fill_concrete_strategy = PaintFillConcreteStrategy(self.get_color_at_point(point))
        paint_fill_concrete_strategy.paint_fill(self, point, color)

class PaintFillConcreteStrategy:
    def __init__(self, color: Color) -> None:
        self._seen_points = set()
        self._original_color = color

    def paint_fill(self, screen: Screen, point: Point, color: Color) -> None:
        if self.should_not_paint_point(screen, point):
            return
        self.record_point(screen, point, color)
        self.check_neighbors(screen, point, color)

    def should_not_paint_point(self, screen: Screen, point: Point) -> bool:
        cartisian_point = (point.get_cartesian_x(), point.get_cartesian_y())

        if cartisian_point in self._seen_points:
            return True
        elif 0 > point.get_cartesian_x():
            return True
        elif screen.get_rows() <= point.get_cartesian_x():
            return True
        elif 0 > point.get_cartesian_y():
            return True
        elif screen.get_columns() <= point.get_cartesian_y():
            return True
        elif str(self._original_color) != str(screen.get_color_at_point(point)):
            return True
        else:
            return False

    def record_point(self, screen: Screen, point: Point, color: Color) -> None:
        cartisian_point = (point.get_cartesian_x(), point.get_cartesian_y())
        self._seen_points.add(cartisian_point)
        screen.set_color_at_point(point, color)

    def check_neighbors(self, screen: Screen, point: Point, color: Color) -> None:
        upper_neighbor_point = Point(point.get_cartesian_x(), point.get_cartesian_y() - 1)
        right_neighbor_point = Point(point.get_cartesian_x() + 1, point.get_cartesian_y())
        lower_neighbor_point = Point(point.get_cartesian_x(), point.get_cartesian_y() + 1)
        left_neighbor_point = Point(point.get_cartesian_x() - 1, point.get_cartesian_y())

        self.paint_fill(screen, upper_neighbor_point, color)
        self.paint_fill(screen, right_neighbor_point, color)
        self.paint_fill(screen, lower_neighbor_point, color)
        self.paint_fill(screen, left_neighbor_point, color)
