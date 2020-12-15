from abc import ABC

class Size:
    LARGE = "Large"
    MEDIUM = "Medium"
    SMALL = "Small"

class Vehicle(ABC):
    def __init__(self, vid):
        self._id = vid
        self._size = ""

    def get_id(self):
        return self._id

    def get_size(self):
        return self._size

class Truck(Vehicle):
    def __init__(self, vid):
        super().__init__(vid)
        self._size = Size.LARGE

class Van(Vehicle):
    def __init__(self, vid):
        super().__init__(vid)
        self._size = Size.MEDIUM

class Car(Vehicle):
    def __init__(self, vid):
        super().__init__(vid)
        self._size = Size.SMALL
