import unittest
from contextlib import suppress
#target = __import__("incidents.py")
import incidents
import os

class TestIncidents(unittest.TestCase):
    def setUp(self):
        client = incidents.api_client

    def test_user(self):
        self.assertEqual(incidents.my_user['id'], 'P8KLUCQ')

    def test_incidents_retrieved(self):
        self.assertIsNotNone(incidents.my_incidents)

    def test_csv_created(self):
        with suppress(OSError):
            os.path.exists('incidents.csv')

if __name__ == '__main__':
    unittest.main()
