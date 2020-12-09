
class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    def __str__(self) -> str:
        return f"({self._red}, {self._green}, {self._blue})"
