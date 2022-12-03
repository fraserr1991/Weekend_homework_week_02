class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.room_guest_list = []
        self.room_in_use_by = {}
        self.guest_in_room = False
        self.song_list = []

    def add_song(self, song):
        self.song_list.append(song)
        return self.song_list

    def check_in_guest(self, guest):
        if self.guest_in_room == False:
            self.room_guest_list.append(guest)
            self.guest_in_room = True
            # print(self.room_guest_list)
            return self.room_guest_list
        else:
            print(f"Room {self.room_number} already in use by {self.room_guest_list}")
            return False

    def check_out_guest(self):
        self.room_guest_list = []
        self.guest_in_room = False
        return self.room_guest_list

    def room_info(self):
        self.room_in_use_by["Room"] = self.room_number
        self.room_in_use_by["Name"] = self.room_guest_list
        return self.room_in_use_by

    # def check_in_guest(self):
    #     print(self.room.append("Bob"))