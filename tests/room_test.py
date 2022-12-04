import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest
from src.drink import Drink

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.instance_of_song = Song("Unholy", "Sam Smith")
        self.instance_of_song_2 = Song("Anti-Hero", "Taylor Swift")

        self.instance_of_song_list = [self.instance_of_song.name_of_song, self.instance_of_song_2.name_of_song]

        self.instance_of_guest_1 = Guest("Bob", 40, 100, "Unholy")
        self.instance_of_guest_2 = Guest("George", 50, 50, "Unholy")
        self.instance_of_guest_3 = Guest("Claire", 14, 200, "Unholy")
        self.instance_of_guest_4 = Guest("Victoria", 60, 10000, "Unholy")
        self.instance_of_guest_5 = Guest("Lewis", 22, 100, "Unholy")

        self.instance_of_room_1 = Room(1, 10, 4)
        self.instance_of_room_2 = Room(2, 10, 5)
        self.instance_of_room_3 = Room(3, 50, 2)
        self.instane_of_room_4 = Room(4, 10, 5)

        self.drink_1 = Drink("Mocha", 2.50)
        self.drink_2 = Drink("Latte", 2.90)
        self.drink_3 = Drink("Flat White", 3.00)


    def test_room_has_number(self):
        self.assertEqual(1, self.instance_of_room_1.room_number)

    def test_add_song(self):
        song_list = self.instance_of_room_1.add_song(self.instance_of_song.name_of_song)
        song_list_2 = self.instance_of_room_2.add_song(self.instance_of_song_2.name_of_song)
        self.assertEqual(["Unholy"], song_list)
        self.assertEqual(["Anti-Hero"], song_list_2)

    def test_add_multiple_songs(self):
        multiple_song_list = self.instance_of_room_1.add_song(self.instance_of_song_list)
        self.assertEqual([['Unholy', 'Anti-Hero']], multiple_song_list) #should probably be in only one list, not two?
    
    def test_checkin_guest_to_room(self):
        guest = self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.assertEqual(["Bob"], guest)

    def test_checkin_guest_to_different_room_numbers(self):
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.instance_of_room_2.check_in_guest(self.instance_of_guest_2.name)
        guests_in_room_2 = self.instance_of_room_2.check_in_guest(self.instance_of_guest_3.name)
        self.instance_of_room_3.check_in_guest(self.instance_of_guest_5.name)
        guests_in_room_3 = self.instance_of_room_3.check_in_guest(self.instance_of_guest_4.name)
        self.assertEqual(["Lewis", "Victoria"], guests_in_room_3)
        self.assertEqual(["George", "Claire"], guests_in_room_2)
    
    def test_checkout_guest_from_room_empty_list(self):
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        guest_check_out = self.instance_of_room_1.check_out_guest(self.instance_of_guest_1.name)
        self.assertEqual([], guest_check_out)

    def test_checkout_guest_from_room(self):
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_2.name)
        guest_check_out = self.instance_of_room_1.check_out_guest(self.instance_of_guest_1.name)
        self.assertEqual(["George"], guest_check_out)
    
    def test_max_guest_number_in_room(self):
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_2.name)
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_3.name)
        self.instance_of_room_1.check_in_guest(self.instance_of_guest_4.name)
        cant_check_in_guest_5 = self.instance_of_room_1.check_in_guest(self.instance_of_guest_5.name)
        self.assertEqual(False, cant_check_in_guest_5)

    def test_guest_pays_fee(self):
        self.instance_of_guest_1.pay_entry_fee_from_wallet(self.instance_of_room_1.room_fee)
        self.assertEqual(90, self.instance_of_guest_1.wallet)

    def test_if_favourite_song_is_on(self):
        self.instance_of_room_1.add_song(self.instance_of_song.name_of_song)
        cheer = self.instance_of_room_1.guests_favourite_song_is_on(self.instance_of_guest_1.favourite_song)
        self.assertEqual("Whooooo!", cheer)

    # def test_fee_taken(self):
    #     self.instance_of_room_1.check_in_guest(self.instance_of_guest_1.name)
    #     self.instance_of_room_2.check_in_guest(self.instance_of_guest_2.name)
    #     self.instance_of_room_2.check_in_guest(self.instance_of_guest_3.name)
    #     self.instance_of_room_3.check_in_guest(self.instance_of_guest_5.name)
    #     fee_taken = self.instance_of_room_3.check_in_guest(self.instance_of_guest_4.room_fee)
    #     self.assertEqual(1130, fee_taken)
        