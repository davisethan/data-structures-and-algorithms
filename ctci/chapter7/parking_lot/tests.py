import unittest
from Parking import ParkingLot, ParkingSpace, FullParkingLotException
from Vehicle import Truck, Van, Car, Size

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        parking_spaces = {
            "A0": ParkingSpace("A0", Size.LARGE, Truck("P0")),
            "A1": ParkingSpace("A1", Size.LARGE, Truck("P1")),
            "A2": ParkingSpace("A2", Size.LARGE, Truck("P2")),
            "B0": ParkingSpace("B0", Size.MEDIUM, Van("Q0")),
            "B1": ParkingSpace("B1", Size.MEDIUM, Van("Q1")),
            "B2": ParkingSpace("B2", Size.MEDIUM, Van("Q2")),
            "C0": ParkingSpace("C0", Size.SMALL, Car("R0")),
            "C1": ParkingSpace("C1", Size.SMALL, Car("R1")),
            "C2": ParkingSpace("C2", Size.SMALL, Car("R2")),
        }

        self.parking_lot = ParkingLot(parking_spaces)

    def test_park_vehicle(self):
        # (case name, vehicle, open parking space, expected)
        cases = [
            ("large_vehicle", Truck("P3"), ParkingSpace("A3", Size.LARGE), "A3"),
            ("medium_vehicle", Van("Q3"), ParkingSpace("B3", Size.MEDIUM), "B3"),
            ("small_vehicle", Car("R3"), ParkingSpace("C3", Size.SMALL), "C3"),
        ]
        for case in cases:
            with self.subTest(case[0]):
                self.parking_lot.add_parking_space(case[2])

                parking_space_id = self.parking_lot.park_vehicle(case[1])

                self.assertEqual(case[3], parking_space_id)

    def test_park_vehicle_with_full_parking_lot_exception(self):
        vehicle = Truck("P3")
        with self.assertRaises(FullParkingLotException):
            self.parking_lot.park_vehicle(vehicle)

    def test_retrieve_vehicle_by_parking_space_id(self):
        parking_space_id = "A0"
        vehicle_id = self.parking_lot.get_parking_spaces()[parking_space_id].get_vehicle().get_id()
        
        vehicle = self.parking_lot.retrieve_vehicle_by_parking_space_id(parking_space_id)

        self.assertEqual(vehicle_id, vehicle.get_id())

if __name__ == "__main__":
    unittest.main()
