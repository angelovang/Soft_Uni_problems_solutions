import unittest
from unittest import TestCase

from Decorators.project_comp_store import Mammal


class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal("Bobi", "Dog", "bau")

    def test_correct_initializing(self):
        self.assertEqual("Bobi",self.mammal.name)
        self.assertEqual('Dog',self.mammal.type)
        self.assertEqual("bau",self.mammal.sound)
        self.assertEqual("animals",self.mammal._Mammal__kingdom)

    def test_make_right_sound(self):
        result = self.mammal.make_sound()
        expected_result = "Bobi makes bau"
        self.assertEqual(expected_result,result)

    def test_get_right_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = self.mammal._Mammal__kingdom
        self.assertEqual(expected_result, result)

    def test_get_right_info(self):
        result = self.mammal.info()
        expected_result = "Bobi is of type Dog"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()