import unittest


class TestClass_Name(unittest.TestCase):

    def setUp(self):
        self.class_name = Clas_Name(a,b)

    def test_correct_initializing(self):
        self.assertEqual(to_be,result)

    def test_if_or_not(self):
        result = self.class_name.metod()
        self.assertEqual(to_be,result)

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.class_name.metod()
        self.assertEqual(to_be, str(ve.exception))

if __name__ == "__main__":
    unittest.main()