import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.instance_of_room_1 = Room(1)
        self.instance_of_room_2 = Room(2)
        self.instance_of_song = Song("Unholy", "Sam Smith")
        self.instance_of_song_2 = Song("Anti-Hero", "Taylor Swift")
        self.instance_of_guest_1 = Guest("Bob", 40)
        self.instance_of_guest_2 = Guest("George", 50)

    def test_room_has_number(self):
        self.assertEqual(1, self.instance_of_room_1.room_number)

    def test_add_song(self):
        song_list = self.instance_of_room_1.add_song(self.instance_of_song.name_of_song)
        self.assertEqual(["Unholy"], song_list)
    
    def test_add_guest_to_room(self):
        guest = self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.assertEqual(["Bob"], guest)
    
    def test_checkout_guest_from_room(self):
        guest_check_out = self.instance_of_room_1.check_out_guest()
        self.assertEqual([], guest_check_out)

    def test_guest_in_room_is_true(self):
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        is_guest_in_room = self.instance_of_room_1.check_in_guest(self.instance_of_guest_2.name)
        self.assertEqual(False, is_guest_in_room)

    def test_guest_in_room_is_false(self):
        is_guest_in_room = self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.assertEqual(["Bob"], is_guest_in_room)
    
    def test_show_people_in_room(self):
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.instance_of_room_2.check_in_guest(self.instance_of_guest_2.name)
        room_info_1 = self.instance_of_room_1.room_info()
        room_info_2 = self.instance_of_room_2.room_info()
        self.assertEqual({'Room': 1, 'Name': ['Bob']}, room_info_1)
        self.assertEqual({'Room': 2, 'Name': ['George']}, room_info_2)


    # def test_room_has_guest(self):
    #     guest_checked_in = Room.check_in_guest()
    #     self.assertEqual(["Bob"], guest_checked_in)
        