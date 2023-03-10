from unittest import TestCase, main

from OOP.TestingExercise.projectVehicle.Vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20.1, 152.5)

    def test_default_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(20.1, self.vehicle.fuel)
        self.assertEqual(152.5, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_no_fuel_raise(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_car(self):
        self.vehicle.drive(2)
        self.assertEqual(17.6, self.vehicle.fuel)

    def test_refuel_too_much_raise(self):
        self.vehicle.fuel = 100
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_ok(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(20)
        self.assertEqual(20, self.vehicle.fuel)

    def test_correct_str(self):
        result = str(self.vehicle)

        expected_result = f"The vehicle has {self.vehicle.horse_power} horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()