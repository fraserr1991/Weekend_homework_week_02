class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.rooms = [
            {"Room Number" : 1, "Guests in room" : 0, "Song list" : [], "Room guests" : []},
            {"Room Number" : 2, "Guests in room" : 0, "Song list" : [], "Room guests" : []},
            {"Room Number" : 3, "Guests in room" : 0, "Song list" : [], "Room guests" : []},
            {"Room Number" : 4, "Guests in room" : 0, "Song list" : [], "Room guests" : []}
        ]

    def add_song(self, song):
        for room in self.rooms:
            if room["Room Number"] == self.room_number:
                room["Song list"].append(song)
                return room["Song list"]

    def check_in_guest(self, guest):
        for room in self.rooms:
            if room["Room Number"] == self.room_number:
                    if room["Guests in room"] < 4:
                        room["Guests in room"] += 1
                        room["Room guests"].append(guest)
                        return room["Room guests"]
                    else:
                        print(f"Sorry room {self.room_number} is full, please choose another")
                        return False

    def check_out_guest(self, guest_name):
        for room in self.rooms:
            if room["Room Number"] == self.room_number:
                for guest in room["Room guests"]:
                    if guest == guest_name:
                        room["Guests in room"] -= 1
                        room["Room guests"].remove(guest_name)
                        return room["Room guests"]