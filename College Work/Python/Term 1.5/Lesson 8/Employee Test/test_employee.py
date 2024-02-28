import unittest
from unittest.mock import patch
from employee import Employee
fr = open("logTestRun.txt","r")
class TestEmployee(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):
        print("SetupClass")        
        fr.read()
    
    @classmethod
    def TearDownClass(cls):
        print("tearDownClass")
        fr.close()

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print("tearDown\n")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')        

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_email(self):
        print('test_email')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.assert_called_with('http://company.com/Schafer/May')            
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


        

if __name__ == "__main__":
    unittest.main()