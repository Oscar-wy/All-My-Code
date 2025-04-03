from room import Room
from character import *
from item import Item
from rpginfo import RPGInfo
dead = False
#Creating Game:
spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

# Creating Rooms:
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge")
dining_hall = Room("dining_hall")
stairwell = Room("stairwell")
coridor = Room("coridor")
# Linking Rooms:
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
coridor.link_room(kitchen, "west")
coridor.link_room(ballroom, "south")
kitchen.link_room(coridor, "east")
ballroom.link_room(coridor, "north")
stairwell.link_room(coridor, "south")
coridor.link_room(stairwell, "north")
#Setting Characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("Cheese")
dining_hall.add_character(dave)
john = Enemy("John", "A vampire")
john.set_conversation("...")
john.set_weakness("Dagger")
ballroom.add_character(john)
catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Hello there.")
ballroom.add_character(catrina)

user = input("What do you want your name to be? ")
userdesc = input("How would you describe yourself? ")
Player = PlayerCharacter(user, userdesc)

current_room = kitchen

print(f"There are {str(Room.numberOfRooms)} rooms to explore")
while not dead:
    print("\n")
    current_room.get_details()
    inhabitants = current_room.get_characters()
    command = input("> ").lower()
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "search":
        for i in inhabitants:
            inhabitants[i].Found = True
    elif command == "talk":
        for i in inhabitants:
            print(f"Talk to {i}?")
            user = input("(y/n)> ").lower()
            if user == "y":
                inhabitants[i].talk()
    elif command == "fight":
        for i in inhabitants:
            print(f"Talk to {i}?")
            user = input("(y/n)> ").lower()
            if user == "y":
                inhabitants[i].talk()
            if inhabitants[i] is not None and isinstance(inhabitants[i], Enemy):
                print("Your items are: ")
                for i in Player.backpack:
                    print(i.Name)
                command = input("What do you want to fight with? ").lower()
                if command in Player.backpack.lower():
                    if inhabitants[i].fight(command):
                        print("You won the fight!")
                        current_room.set_character(None)
                    else:
                        print("You lost the fight.")
                        dead = True
                else:
                    print("You don't have that item")
            else:
                print("There is no one here to fight with")
    elif command == "hug":
        for i in inhabitants:
            print(f"Talk to {i}?")
            user = input("(y/n)> ").lower()
            if user == "y":
                inhabitants[i].talk()
            if inhabitants[i] is not None:
                if isinstance(inhabitants[i], Enemy):
                    print("I wouldn't do that if I were you...")
                else:
                    inhabitants[i].hug()
            else:
                print("There is no one here to hug :(")
    elif command == "open":
        pass
    elif command == "collect":
        pass
    current_room = current_room.move(command)
print("Game Over!")
RPGInfo.credits()