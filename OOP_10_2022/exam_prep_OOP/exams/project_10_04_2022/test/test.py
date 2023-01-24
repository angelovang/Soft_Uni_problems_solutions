import unittest
from exams.project_10_04_2022.movie import Movie


class TestMovie(unittest.TestCase):

    def setUp(self):
        self.movie = Movie("Trap", 2001, 10.5)
        self.movie_2 = Movie("Stars", 2010, 11)

    def test_correct_initializing(self):
        self.assertEqual("Trap", self.movie.name)
        self.assertEqual(2001, self.movie.year)
        self.assertEqual(10.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_not_be_empty(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie("", 1999, 10.5)
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_not_be_less_than_1887(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie("Abc", 1886, 10.5)
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_is_in_the_list(self):
        self.movie.actors = ["Ben"]
        result = self.movie.add_actor("Ben")
        self.assertEqual("Ben is already added in the list of actors!", result)

    def test_add_actor_is_added_to_the_list(self):
        self.movie.add_actor("Ben")
        self.movie.add_actor("Ann")
        self.assertEqual(["Ben","Ann"], self.movie.actors )
        self.assertEqual(2, len(self.movie.actors))

    def test_rating_gt_(self):
        self.movie.rating = 20
        result = self.movie.__gt__(self.movie_2)
        self.assertEqual('"Trap" is better than "Stars"', result)

    def test_rating_gt_reverse(self):
        result = self.movie.__gt__(self.movie_2)
        self.assertEqual('"Stars" is better than "Trap"', result)

    def test_correct_repr_(self):
        self.movie.actors = ["Ben", "Ann"]
        result = self.movie.__repr__()
        self.assertEqual("Name: Trap\nYear of Release: 2001\nRating: 10.50\nCast: Ben, Ann", result)


if __name__ == "__main__":
    unittest.main()

