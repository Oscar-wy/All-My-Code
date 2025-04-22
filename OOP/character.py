class Character:
    def __init__(self, nameInp, ageInp):
        self.Name = nameInp
        self.Age = ageInp
        self.Description = ""
    def getName(self):
        return self.Name
    def setDescription(self, description):
        self.Description = description
    def Describe(self):
        return self.Describe
    
class Enemy(Character):
    def __init__(self, nameInp, ageInp):
        super().__init__(nameInp, ageInp)
    def Fight():
        pass

class Player(Character):
    def __init__(self, nameInp, ageInp):
        super().__init__(nameInp, ageInp)
        self.Inventory = {}
        self.InventorySpace = 5
        self.Health = 100
        self.CurrentWeapon = None
        self.CurrentArmour = None
    def setArmour(self, Armour):
        self.CurrentArmour = Armour
    def setWeapon(self, Weapon):
        self.CurrentWeapon = Weapon
    def getInventory(self):
        return self.Inventory
    def Pickup(self, Item):
        if len(self.Inventory) < self.InventorySpace:
            self.Inventory[Item.Name] = Item
            return True
        else:
            print("You dont have enough space!")
            return False
    def Drop(self, Item):
        if Item.Name in self.Inventory:
            self.Inventory.remove(Item.Name)
            return True
        else:
            print("Item not in inventory!")
            return False