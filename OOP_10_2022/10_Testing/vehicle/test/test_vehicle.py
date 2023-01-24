import unittest

from Test.vehicle.project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(40.5, 136)

    # def test_right_DEFAULT_FUEL_CONSUMPTION(self):
    #     self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initializing(self):
        self.assertEqual(40.5, self.vehicle.fuel)
        self.assertEqual(40.5, self.vehicle.capacity)
        self.assertEqual(136, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_is_fuel_enough_to_drive_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_fuel_enough_to_drive_decrease_self_fuel(self):
        self.vehicle.drive(10)
        result = self.vehicle.fuel
        expected_result = 40.5 - 10 * 1.25
        self.assertEqual(expected_result, result)

    def test_refuel_too_much_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_fuel_increase(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)

        self.assertEqual(10, self.vehicle.fuel)

    def test_correct__str__(self):
        result = str(self.vehicle)
        expected_result = "The vehicle has 136 horse power " \
                          "with 40.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
