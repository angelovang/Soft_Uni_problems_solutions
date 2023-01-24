import unittest

from Test.student.project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student("abc")
        self.student_2 = Student("klm", {"prog": ["Java", "C#"]})

    def test_correct_initializing(self):
        self.assertEqual("abc", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)
        self.assertEqual({"prog": ["Java", "C#"]}, self.student_2.courses)

    def test_enroll_course_name_in_courses(self):
        self.student_2.courses = {"prog": []}
        result = self.student_2.enroll("prog", ["Java", "C#"], "")
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(expected_result, result)
        self.assertEqual(["Java", "C#"], self.student_2.courses["prog"])

    def test_enroll_course_not_present_add_course_notes_Yes(self):
        result = self.student_1.enroll("math", ["a", "b", "c"], "Y")

        self.assertEqual(["a", "b", "c"], self.student_1.courses["math"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_not_present_add_course_notes_without_third_parameter(self):
        result = self.student_1.enroll("math", ["a", "b", "c"])

        self.assertEqual(["a", "b", "c"], self.student_1.courses["math"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_not_present_add_course_name(self):
        result = self.student_1.enroll("math", ["a", "b", "c"], "N")

        self.assertEqual([], self.student_1.courses["math"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("math", [1, 2, 3])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_correct_add_notes(self):
        result = self.student_2.add_notes("prog", "Python")

        self.assertEqual(["Java", "C#", "Python"] , self.student_2.courses["prog"])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_cannot_be_removed(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("prog")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_is_removed(self):
        result = self.student_2.leave_course("prog")

        self.assertEqual({}, self.student_2.courses)
        self.assertEqual("Course has been removed", result)


if __name__ == "__main__":
    unittest.main()
