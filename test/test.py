import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_home(self):
        tester = app.test_client()
        response = tester.get('/')  # Update path to '/'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"!Dnyanoba!")  # Correct the expected output

if __name__ == "__main__":
    unittest.main()
