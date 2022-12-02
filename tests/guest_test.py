import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.instance_of_guest = Guest("Bob", 40)
    
    def test_guest_has_name(self):
        self.assertEqual("Bob", self.instance_of_guest.name)
    
    def test_guest_has_age(self):
        self.assertEqual(40, self.instance_of_guest.age)