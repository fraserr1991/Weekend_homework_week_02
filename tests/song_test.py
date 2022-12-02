import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.instance_of_song = Song("Unholy", "Sam Smith")
    
    def test_song_has_name(self):
        self.assertEqual("Unholy", self.instance_of_song.name_of_song)
    
    def test_song_has_artist(self):
        self.assertEqual("Sam Smith", self.instance_of_song.artist)

# Unholy (feat. Kim Petras)Sam Smith, Kim Petras.
# Anti-HeroTaylor Swift.
# Made You LookMeghan Trainor.