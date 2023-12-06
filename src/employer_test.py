import unittest
from src.employee import Employee

class  EmployeeVaseTest(unittest.TestCase):

    def test_create_employee_ideal(self):
        instance = Employee(name= '1', surname= '2', age=20)
        self.assertEqual(instance.name, second= '1')
        self.assertEqual(instance.surname, second= '2')