from src.guest import Guest

class Room:
    def __init__(self, room_number, room_fee, capacity, drinks_list):
        self.room_number = room_number
        self.room_guest_list = []
        self.guests_in_room = 0
        self.song_list = []
        self.room_capacity = capacity
        self.room_fee = room_fee
        self.bar_tab = 0
        self.total_charge = 0
        self.total_fee = 0
        self.drinks_list = drinks_list


    def add_song(self, song):
        self.song_list.append(song)
        # print(self.song_list)
        return self.song_list

    def check_in_guest(self, guest):
        if self.guests_in_room < self.room_capacity:
            self.room_guest_list.append(guest)
            self.guests_in_room += 1 
            self.total_fee += self.room_fee
            #print(f"Room number: {self.room_number}, Total collected fee's: {self.total_fee}, Guests in room: {self.guests_in_room}, Room guest list: {self.room_guest_list}, Song list: {self.song_list}")
            return self.room_guest_list
        else:
            #print(f"Sorry room {self.room_number} is full")
            return False

    def check_out_guest(self, guest_name):
        for guest in self.room_guest_list:
            if guest == guest_name:
                self.guests_in_room -= 1
                self.room_guest_list.remove(guest_name)
                # print(self.room_guest_list)
                return self.room_guest_list
    
    def guests_favourite_song_is_on(self, favourite_song):
        for song in self.song_list:
            if song == favourite_song:
                return "Whooooo!"

    def find_drink(self, drink_name):
        for name_of_drink in self.drinks_list:
            if name_of_drink.name == drink_name:
                return name_of_drink
    
    def add_drink_to_tab(self, amount):
        self.bar_tab += amount