from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.b_store = Bookstore(100)

    def test_correct_initializing_book_greet_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.b_store = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))
        self.assertEqual(100, self.b_store.books_limit)
        self.assertEqual({}, self.b_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.b_store.total_sold_books)

    def test_correct_count_total_number_of_books(self):
        self.b_store.availability_in_store_by_book_titles = {
            "abc": 5,
            "def": 5,
        }
        self.assertEqual(10 , self.b_store.__len__())

    def test_receive_book_if_there_is_not_enough_space(self):
        self.b_store.books_limit = 1
        with self.assertRaises(Exception) as ex:
            self.b_store.receive_book("abc", 10)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_if_there_is_enough_space_book_title_not_in(self):
        self.b_store.receive_book("abc", 10)
        self.assertEqual(10 , self.b_store.availability_in_store_by_book_titles["abc"])

    def test_test_receive_book_take_the_new_availability(self):
        self.b_store.receive_book("abc", 10)
        result = self.b_store.receive_book("abc", 10)
        self.assertEqual("20 copies of abc are available in the bookstore.", result)

    def test_sell_book_if_book_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.b_store.sell_book("cde", 5)

        self.assertEqual("Book cde doesn't exist!", str(ex.exception))

    def test_sell_book_if_there_not_enough_copies_to_sell(self):
        self.b_store.receive_book("abc", 10)
        with self.assertRaises(Exception) as ex:
            self.b_store.sell_book("abc", 15)

        self.assertEqual(f"abc has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_book_if_sell_is_successfully(self):
        self.b_store.receive_book("abc", 15)
        result = self.b_store.sell_book("abc", 10)
        self.assertEqual("Sold 10 copies of abc", result)

    def test_cell_total_sold_books(self):
        self.b_store.receive_book("abc", 15)
        self.b_store.sell_book("abc", 10)
        result = self.b_store.total_sold_books
        self.assertEqual(10 , result)

    def test_correct_str_presentation(self):
        self.b_store.receive_book("abc", 15)
        self.b_store.receive_book("dce", 10)
        self.b_store.sell_book("abc", 10)
        result = self.b_store.__str__()
        self.assertEqual("Total sold books: 10\nCurrent availability: 15\n - abc: 5 copies\n - dce: 10 copies", result)


if __name__ == "__main__":
    unittest.main()
