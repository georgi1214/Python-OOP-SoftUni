from unittest import TestCase, main

from Mini_projects.MiniProjectsWithRandom.projectMovieLibrrary import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student("Pesho")
        self.student_with_courses = Student("Ivan",  {"Python": ["note1"]})

    def test_correct_init(self):
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Python": ["note1"]}, self.student_with_courses.courses)

    def test_enroll_existing_course_with_param(self):
        result = self.student_with_courses.enroll("Python", ["note2", "note3"], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note1", "note2", "note3"], self.student_with_courses.courses["Python"])

    def test_enroll_existing_course_no_param(self):
        result = self.student_with_courses.enroll("Python", ["note3", "note4"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(3, len(self.student_with_courses.courses["Python"]))
        self.assertEqual(self.student_with_courses.courses["Python"], ["note1", "note3", "note4"])

    def test_enroll_no_course(self):
        result = self.student.enroll("Math", ["note1"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1"], self.student.courses["Math"])

    def test_enroll_no_course_param(self):
        result = self.student.enroll("Math", ["note1"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["note1"], self.student.courses["Math"])

    def test_enroll_no_course_dont_add_notes(self):
        result = self.student.enroll("Math", ["note1"], "N")
        self.assertEqual({"Math": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_existing_course(self):
        result = self.student_with_courses.add_notes("Python", "note3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(self.student_with_courses.courses, {"Python": ["note1", "note3"]})

    def test_add_note_not_existing_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Math", "note1")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_exists(self):
        result = self.student_with_courses.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_no_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Math")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()