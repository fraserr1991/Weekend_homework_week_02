import unittest

from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.instance_of_room = Room(1)
        self.instance_of_guest_1 = Guest("Bob", 40)

    def test_room_has_number(self):
        self.assertEqual(1, self.instance_of_room.room_number)

    # def test_room_has_guest(self):
    #     guest_checked_in = .check_in_guest()
    #     self.assertEqual(["Bob"], guest_checked_in)
        