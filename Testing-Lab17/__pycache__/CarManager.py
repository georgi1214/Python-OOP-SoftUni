from unittest import TestCase, main

# from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Nisan", "GT-R", 15, 75)

    def test_correct_init(self):
        self.assertEqual("Nisan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_zero_neg_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_capacity_zero_neg_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_neg_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_neg_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more(self):
        self.car.refuel(78)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_less(self):
        self.car.refuel(50)
        result = self.car.fuel_capacity - self.car.fuel_amount
        self.assertEqual(result, 25)


    def test_drive_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(0.1)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()