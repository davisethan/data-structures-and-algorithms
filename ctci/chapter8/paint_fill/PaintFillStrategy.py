from abc import ABC
from Color import Color
from Point import Point
from Screen import Screen

class PaintFillStrategy(ABC):
    def __init__(self, screen: Screen, point: Point, color: Color) -> None:
        self._screen = screen
        self._point = point
        self._color = color

    def paint_fill(self) -> None:
        pass

class RecursivePaintFillStrategy(PaintFillStrategy):
    def __init__(self, screen: Screen, point: Point, color: Color) -> None:
        super().__init__(screen, point, color)

        # Values
        self._UP = "UP"
        self._RIGHT = "RIGHT"
        self._DOWN = "DOWN"
        self._LEFT = "LEFT"

        # Constants
        self._original_color = self._screen.get_color_at_point(self._point)

        # Variables
        self._seen_points = set()
    
    def paint_fill(self) -> None:
        if self.shouldnt_paint_point():
            return
        self.paint_point()
        self.paint_neighbor_points()

    def shouldnt_paint_point(self) -> bool:
        if str(self._point) in self._seen_points:
            return True
        elif 0 > self._point.get_x():
            return True
        elif self._screen.get_rows() <= self._point.get_x():
            return True
        elif 0 > self._point.get_y():
            return True
        elif self._screen.get_columns() <= self._point.get_y():
            return True
        elif str(self._original_color) != str(self._screen.get_color_at_point(self._point)):
            return True
        else:
            return False

    def paint_point(self) -> None:
        self._seen_points.add(str(self._point))
        self._screen.set_color_at_point(self._point, self._color)

    def paint_neighbor_points(self) -> None:
        self.paint_neighbor_point(self._UP)
        self.paint_neighbor_point(self._RIGHT)
        self.paint_neighbor_point(self._DOWN)
        self.paint_neighbor_point(self._LEFT)

    def paint_neighbor_point(self, neighbor_name) -> None:
        neighbor_point = self.create_neighbor_point(neighbor_name)
        current_point = self._point
        self._point = neighbor_point
        self.paint_fill()
        self._point = current_point

    def create_neighbor_point(self, neighbor_name) -> None:
        if self._UP == neighbor_name:
            return Point(self._point.get_x(), self._point.get_y() - 1)
        elif self._RIGHT == neighbor_name:
            return Point(self._point.get_x() + 1, self._point.get_y())
        elif self._DOWN == neighbor_name:
            return Point(self._point.get_x(), self._point.get_y() + 1)
        elif self._LEFT == neighbor_name:
            return Point(self._point.get_x() - 1, self._point.get_y())
        else:
            print("Create neighbor point error")
