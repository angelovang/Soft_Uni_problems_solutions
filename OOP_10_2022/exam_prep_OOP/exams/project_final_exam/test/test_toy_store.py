from exams.project_final_exam.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):

    def setUp(self):
        self.toy_st = ToyStore()

    def test_correct_initializing(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        },self.toy_st.toy_shelf)

    def test_add_toy_shelf_not_in_keys(self):
        with self.assertRaises(Exception) as ex:
            self.toy_st.add_toy("N", "abc")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_toy_is_in_list(self):
        self.toy_st.toy_shelf["A"] = "abc"
        with self.assertRaises(Exception) as ex:
            self.toy_st.add_toy("A", "abc")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_Toy_is_taken(self):
        self.toy_st.toy_shelf["A"] = "def"
        with self.assertRaises(Exception) as ex:
            self.toy_st.add_toy("A", "abc")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_is_successful(self):
        result = self.toy_st.add_toy("A", "abc")
        self.assertEqual({
            "A": "abc",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_st.toy_shelf)
        self.assertEqual("Toy:abc placed successfully!",result)

    def test_remove_toy_shelf_not_in_the_list(self):
        self.toy_st.toy_shelf["A"] = "abc"
        with self.assertRaises(Exception) as ex:
            self.toy_st.remove_toy("N","abc")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_toy_doesnt_exist(self):
        self.toy_st.toy_shelf["A"] = "abc"
        with self.assertRaises(Exception) as ex:
            self.toy_st.remove_toy("A", "def")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_toy_doesnt_exist_none(self):
        with self.assertRaises(Exception) as ex:
            self.toy_st.remove_toy("A", "def")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successfully(self):
        self.toy_st.toy_shelf["A"] = "abc"
        self.toy_st.toy_shelf["B"] = "def"
        result = self.toy_st.remove_toy("A","abc")
        self.assertEqual({
            "A": None,
            "B": "def",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_st.toy_shelf)
        self.assertEqual("Remove toy:abc successfully!", result)



if __name__ == "__main__":
    unittest.main()