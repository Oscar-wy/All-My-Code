from room import Room
from character import *
from item import Item
# Creating Rooms:
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge")
dining_hall = Room("dining_hall")
# Linking Rooms:
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("Cheese")
dining_hall.set_character(dave)
john = Enemy("John", "A vampire")
john.set_conversation("...")
john.set_weakness("Dagger")
ballroom.set_character(john)

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ").lower()
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "fight":
        command = input("What do you want to fight with? ").lower()
        if not inhabitant.fight(command):
            break
    current_room = current_room.move(command)
print("Game Over!")