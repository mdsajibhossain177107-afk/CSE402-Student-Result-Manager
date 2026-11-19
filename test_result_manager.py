
import unittest
from contextlib import redirect_stdout
from io import StringIO

from student_result_manager import (
    Student,
    Course,
    ResultManager,
    calculate_grade
)


class TestStudentResultManager(unittest.TestCase):

    def setUp(self):
        self.manager = ResultManager()

    def test_grade_calculation(self):
        self.assertEqual(calculate_grade(85), ("A+", 4.00))
        self.assertEqual(calculate_grade(77), ("A", 3.75))
        self.assertEqual(calculate_grade(72), ("A-", 3.50))
        self.assertEqual(calculate_grade(35), ("F", 0.00))

    def test_invalid_marks(self):
        with self.assertRaises(ValueError):
            calculate_grade(110)

        with self.assertRaises(ValueError):
            calculate_grade(-5)

    def test_add_student(self):
        self.manager.add_student("101", "Rahim")

        self.assertIn("101", self.manager.students)

    def test_duplicate_student(self):
        self.manager.add_student("101", "Rahim")

        with redirect_stdout(StringIO()):
            self.manager.add_student("101", "Karim")

        self.assertEqual(
            self.manager.students["101"].name,
            "Rahim"
        )

    def test_add_course(self):
        self.manager.add_course("CSE101", "Programming", 3.0)

        self.assertIn("CSE101", self.manager.courses)

    def test_enter_marks(self):
        self.manager.add_student("101", "Rahim")
        self.manager.add_course("CSE101", "Programming", 3.0)

        self.manager.enter_marks("101", "CSE101", 85)

        self.assertEqual(
            self.manager.students["101"].marks["CSE101"],
            85
        )

    def test_invalid_marks_entry(self):
        self.manager.add_student("101", "Rahim")
        self.manager.add_course("CSE101", "Programming", 3.0)

        with redirect_stdout(StringIO()):
            self.manager.enter_marks("101", "CSE101", 120)

        self.assertNotIn(
            "CSE101",
            self.manager.students["101"].marks
        )

    def test_cgpa_calculation(self):
        self.manager.add_student("101", "Rahim")
        self.manager.add_course("CSE101", "Programming", 3.0)
        self.manager.add_course("CSE102", "Database", 1.0)

        self.manager.enter_marks("101", "CSE101", 80)
        self.manager.enter_marks("101", "CSE102", 70)

        cgpa = self.manager.calculate_cgpa("101")

        self.assertAlmostEqual(cgpa, 3.875)

    def test_result_sheet(self):
        self.manager.add_student("101", "Rahim")
        self.manager.add_course("CSE101", "Programming", 3.0)
        self.manager.enter_marks("101", "CSE101", 85)

        output = StringIO()

        with redirect_stdout(output):
            self.manager.get_result_sheet("101")

        self.assertIn("Rahim", output.getvalue())
        self.assertIn("CGPA", output.getvalue())


if __name__ == "__main__":
    unittest.main()
  
