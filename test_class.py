import unittest
from class_definitions import Student as Students

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Students.Students('Lehmann','Ben', 'Math', gpa=3.0)
    def tearDown(self):
        del self.student
    def  test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Ben')
        self.assertEqual(self.student.last_name, 'Lehmann')
    def test_object_created_all_attributes(self):
        student = Students.Students('Lehmann','Ben', 'Math', gpa=3.0)
        assert student.last_name == 'Lehmann'
        assert student.first_name == 'Ben'
        assert student.major == 'Math'
        assert student.gpa == 3.0
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = Students.Students('123','Ben','Math', 3.0)
    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = Students.Students('123', 'Lehmann', 'Math', 3.0)
    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = Students.Students('Lehmann','Ben','123',3.0)
    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = Students.Students('Lehmann','Ben','Math', 3.8)

if __name__ == '__main__':
    unittest.main()
