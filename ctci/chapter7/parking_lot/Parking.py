from Vehicle import Size

class ParkingLot:
    def __init__(self, parking_spaces = {}):
        self._parking_spaces = parking_spaces

    def get_parking_spaces(self):
        return self._parking_spaces

    def add_parking_space(self, parking_space):
        parking_space_id = parking_space.get_id()
        self._parking_spaces[parking_space_id] = parking_space

    def park_vehicle(self, vehicle):
        parking_space = self._find_open_parking_space(vehicle)

        if None == parking_space:
            raise FullParkingLotException
        
        parking_space.add_vehicle(vehicle)
        return parking_space.get_id()

    def _find_open_parking_space(self, vehicle):
        for parking_space in self._parking_spaces.values():
            if None == parking_space.get_vehicle() and vehicle.get_size() == parking_space.get_size():
                return parking_space

    def retrieve_vehicle_by_parking_space_id(self, pid):
        for parking_space in self._parking_spaces.values():
            if pid == parking_space.get_id():
                return parking_space.remove_vehicle()

class ParkingSpace:
    def __init__(self, pid, size, vehicle = None):
        self._id = pid
        self._size = size
        self._vehicle = vehicle

    def get_id(self):
        return self._id

    def get_size(self):
        return self._size

    def get_vehicle(self):
        return self._vehicle

    def add_vehicle(self, vehicle):
        self._vehicle = vehicle

    def remove_vehicle(self):
        vehicle = self._vehicle
        self._vehicle = None
        return vehicle

class FullParkingLotException(Exception):
    pass
