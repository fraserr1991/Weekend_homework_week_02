class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.room_guest = []
        self.guest_in_room = False
        self.song_list = []

    def add_song(self, song):
        self.song_list.append(song)
        return self.song_list

    def check_in_guest(self, guest):
        if self.guest_in_room == False:
            self.room_guest.append(guest)
            self.guest_in_room = True
            return self.room_guest
        else:
            return False

    def check_out_guest(self):
        self.room_guest = []
        self.guest_in_room = False
        return self.room_guest

    # def room_info(self):
    #     return self.room_number

    # def check_in_guest(self):
    #     print(self.room.append("Bob"))