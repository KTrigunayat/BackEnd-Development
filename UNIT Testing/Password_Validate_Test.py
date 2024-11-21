import unittest
from Password_Validate import validate_password  # Import the function directly

class TestPasswordValidation(unittest.TestCase):
    def test_password_valid(self):
        # Test a valid password
        result = validate_password("Password@123")
        self.assertEqual(result,True)
        result2 = validate_password("password@123")
        self.assertEqual(result2,False)
        result3 = validate_password("PASSWORD@123")
        self.assertEqual(result3,False)
        result4 = validate_password("PASSWORD123")
        self.assertEqual(result4,False)
        result5 = validate_password("Password")
        self.assertEqual(result5,False)
        result6 = validate_password("PASSWORD")
        self.assertEqual(result6,False)
        result7 = validate_password("Pa@123")
        self.assertEqual(result7,False)
        result8 = validate_password("Kshitiz123!")
        self.assertEqual(result8,True)
        result9 = validate_password("Kshitiz123!@#")
        self.assertEqual(result9,True)
        result10 = validate_password("nick@password")
        self.assertEqual(result10,False)
if __name__ == '__main__':
    unittest.main()