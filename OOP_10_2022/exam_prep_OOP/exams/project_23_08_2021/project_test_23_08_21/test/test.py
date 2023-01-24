from exams.project_23_08_2021.project_test_23_08_21.library import Library
import unittest


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library("abc")

    def test_correct_initializing(self):
        self.assertEqual("abc", self.lib.name)
        self.assertEqual({}, self.lib.books_by_authors)
        self.assertEqual({}, self.lib.readers)

    def test_correct_name_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.lib = Library('')
        self.assertEqual("Name cannot be empty string!", str(ve.exception) )

    def test_add_book_author_correct_addition(self):
        self.lib.add_book("an","hide")
        self.assertEqual({"an":["hide"]}, self.lib.books_by_authors)
        self.assertEqual(1 , len(self.lib.books_by_authors))
        self.assertEqual(1, len(self.lib.books_by_authors["an"]))

    def test_add_book_extend_list(self):
        self.lib.add_book("an", "hide")
        self.lib.add_book("an","echo")
        self.lib.add_book("ben", "horror")
        self.assertEqual({"an": ["hide","echo"],"ben": ["horror"]}, self.lib.books_by_authors)
        self.assertEqual(2, len(self.lib.books_by_authors))
        self.assertEqual(2, len(self.lib.books_by_authors["an"]))

    def test_add_reader_in_list(self):
        self.lib.readers = {"Ivan": []}
        result = self.lib.add_reader("Ivan")
        self.assertEqual("Ivan is already registered in the abc library.", result)

    def test_add_reader_not_in_theList(self):
        self.lib.add_reader("Ivan")
        self.lib.add_reader("Peter")
        self.assertEqual({"Ivan": [], "Peter": []}, self.lib.readers)
        self.assertEqual(2, len(self.lib.readers))

    def test_rent_book_reader_name_not_in_teh_list(self):
        result = self.lib.rent_book("Ivan","an","hide")
        self.assertEqual("Ivan is not registered in the abc Library.", result)

    def test_rent_book_author_not_in_the_list(self):
        self.lib.add_reader("Ivan")
        result = self.lib.rent_book("Ivan", "an", "hide")
        self.assertEqual("abc Library does not have any an's books.", result)

    def test_rent_book_book_title_not_in_the_list(self):
        self.lib.add_reader("Ivan")
        self.lib.add_book("an", "hide")
        result = self.lib.rent_book("Ivan", "an", "echo")
        self.assertEqual("""abc Library does not have an's "echo".""", result)

    def test_book_rent_all_is_ok(self):
        self.lib.add_reader("Ivan")
        self.lib.add_book("an", "hide")
        self.lib.add_book("an", "echo")
        self.lib.rent_book("Ivan", "an", "echo")
        self.assertEqual({"Ivan":[{"an": "echo"}]}, self.lib.readers)
        self.assertEqual({"an":["hide"]}, self.lib.books_by_authors)
        self.assertEqual(1 , len(self.lib.readers["Ivan"]))
        self.assertEqual(1, len(self.lib.books_by_authors["an"]))


if __name__ == "__main__":
    unittest.main()
