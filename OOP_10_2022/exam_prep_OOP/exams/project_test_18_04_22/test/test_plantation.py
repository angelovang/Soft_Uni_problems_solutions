from project_test_18_04_22.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):

    def setUp(self):
        self.plant = Plantation(20)
        self.plant_1 = Plantation(10)
        self.plant_1.plants = {"Ivan": ["abc","cde"]}
        self.plant_1.workers.append("Ivan")

    def test_correct_initializing_plantation(self):
        self.assertEqual(20, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_not_correct_plant_size(self):
        with self.assertRaises(ValueError) as ve:
            self.plant = Plantation(-1)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_is_worker_already_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.plant_1.hire_worker("Ivan")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_is_hired(self):
        result = self.plant_1.hire_worker("Gosho")
        self.assertEqual( f"Gosho successfully hired.", result)
        self.assertEqual(2 , len(self.plant_1.workers))

    def test_len_calculation_zero(self):
        result = self.plant.__len__()
        self.assertEqual(0, result)

    def test_len_calculation(self):
        result = self.plant_1.__len__()
        self.assertEqual(2, result)

    def test_correct_plant_size_add_plants(self):
        self.plant_1.planting("Ivan", "efg")
        self.plant_1.hire_worker("Peter")
        self.plant_1.planting("Peter", "asa")
        self.assertEqual(4, len(self.plant_1))


    #
    # def test_len_not_addition(self):
    #     self.pl = Plantation(1)
    #     self.pl.hire_worker('Martin')
    #     self.pl.hire_worker('Alexandra')
    #     self.pl.plants['Martin'] = ['Tomatoes']
    #     self.pl.plants['Alexandra'] = ['plant']
    #     self.assertEqual(self.pl.__len__(), 2)


    def test_planting_if_worker_not_in_self_workers(self):
        with self.assertRaises(ValueError) as ve:
            self.plant.planting('Gosho',"abc")
        self.assertEqual(f"Worker with name Gosho is not hired!", str(ve.exception))

    def test_planting_if_plantation_is_full(self):
        self.plant_1.size = 2
        with self.assertRaises(ValueError) as ve:
            self.plant_1.planting("Ivan", "abc")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_worker_in_plant_keys(self):
        result = self.plant_1.planting("Ivan", "klm")
        self.assertEqual("Ivan planted klm.", result)
        self.assertEqual(3, len(self.plant_1.plants["Ivan"]))

    def test_planting_worker_plant_first_plant(self):
        self.plant_1.workers.append("Gosho")
        result = self.plant_1.planting('Gosho',"klm")
        self.assertEqual("Gosho planted it's first klm.", result)
        self.assertEqual(1, len(self.plant_1.plants["Gosho"]))

    def test_correct_str_presentation(self):
        result = str(self.plant_1)
        self.assertEqual("Plantation size: 10\nIvan\nIvan planted: abc, cde", result)

    def test_correct_rpr_presentation(self):
        self.plant_1.workers.append("Gosho")
        result = self.plant_1.__repr__()
        self.assertEqual("Size: 10\nWorkers: Ivan, Gosho", result)


if __name__ == "__main__":
    unittest.main()