import unittest
from Paint import Screen, Point, Color

class TestPaintFill(unittest.TestCase):
    def test_paint_fill_one_point_one_color(self):
        """BUILD-OPERATE-TEST pattern used."""
        # Build
        before_screen = Screen(1, 1, Color(0, 0, 0))
        after_screen = Screen(1, 1, Color(255, 255, 255))

        # Operate
        before_screen.paint_fill(Point(0, 0), Color(255, 255, 255))

        # Test
        self.assertEqual(str(after_screen), str(before_screen))

    def test_paint_fill_four_points_one_color(self):
        before_screen = Screen(2, 2, Color(0, 0, 0))
        after_screen = Screen(2, 2, Color(255, 255, 255))

        before_screen.paint_fill(Point(0, 0), Color(255, 255, 255))

        self.assertEqual(str(after_screen), str(before_screen))

    def test_paint_fill_nine_point_one_color(self):
        before_screen = Screen(3, 3, Color(0, 0, 0))
        after_screen = Screen(3, 3, Color(255, 255, 255))

        before_screen.paint_fill(Point(0, 0), Color(255, 255, 255))

        self.assertEqual(str(after_screen), str(before_screen))

    def test_paint_fill_nine_points_two_colors(self):
        before_screen = Screen(3, 3, Color(0, 0, 0))
        after_screen = Screen(3, 3, Color(0, 0, 0))
        for row in range(2):
            for column in range(2):
                before_screen.set_color_at_point(Point(row, column), Color(128, 128, 128))
                after_screen.set_color_at_point(Point(row, column), Color(255, 255, 255))

        before_screen.paint_fill(Point(0, 0), Color(255, 255, 255))

        self.assertEqual(str(after_screen), str(before_screen))

if __name__ == "__main__":
    unittest.main()
