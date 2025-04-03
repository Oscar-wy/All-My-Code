class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.Found = False
    def describe(self):
        return self.description
    def set_conversation(self, conversation):
        self.conversation = conversation
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def fight(self, combat_item):
        if combat_item == self.weakness.lower():
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you. puny adventurer")
            return False
    def set_weakness(self, weakness):
        self.weakness = weakness
    def steal(self):
        print(f"You steal from {self.name}")

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def hug(self):
        print(f"{self.name} hugs you?")

class PlayerCharacter(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.backpack = {}