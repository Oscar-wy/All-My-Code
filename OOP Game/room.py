class Room:
    numberOfRooms = 0
    def __init__(self, roomName):
        self.name = roomName
        self.description = None
        self.linked_rooms = {}
        self.characters = {}
        self.items = {}
        Room.numberOfRooms = Room.numberOfRooms + 1
    def describe(self):
        return self.description
    def set_description(self, room_description):
        self.description = room_description
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print(f"{self.name} linked rooms: {repr(self.linked_rooms)}")
    def set_name(self, roomName):
        self.name = roomName
    def get_name(self):
        return self.name
    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    def add_character(self, char):
        self.characters[char.name] = char
    def get_characters(self):
        return self.characters
    def remove_character(self, charName):
        list.remove(self.characters, charName)