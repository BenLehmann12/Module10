import unittest
from class_definitions import Student as Students

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Students.Students('Lehmann','Ben', 'Math', gpa=3.8)
    def tearDown(self):
        del self.student

    def  test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Ben')
        self.assertEqual(self.student.last_name, 'Lehmann')
    def test_object_created_all_attributes(self):
        student = Students.Students('Lehmann','Ben', 'Math', gpa=3.8)
        assert student.last_name == 'Lehmann'
        assert student.first_name == 'Ben'
        assert student.major == 'Math'
        assert student.gpa == 3.8



if __name__ == '__main__':
    unittest.main()
