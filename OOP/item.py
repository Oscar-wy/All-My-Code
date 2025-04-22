class Item:
    def __init__(self, name, type):
        self.Name = name
        self.Type = type
        self.description = None
    def getName(self):
        return self.Name
    def setDescription(self, description):
        self.Description = description
    def Describe(self):
        return self.Describe
    

class Weapon(Item):
    def __init__(self, name, type, damage, durability):
        super().__init__(name, type)
        self.Damage = damage
        self.Durability = durability
    def Attack(self):
        self.Durability -= 1
        return self.Damage

class Armour(Item):
    def __init__(self, name, type, health):
        super().__init__(name, type)
        self.Health = health
    def Damaged(self, damage):
        if self.Health - damage <= 0:
            damage -= self.Health
            self.Health = 0
            return False, damage
        else:
            self.Health -= damage
            return True
        
class Potion(Item):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.Effects = {"Health": [50], "Damage": [-50]}
        self.Effect = self.Effects[type]
    def Use(self):
        pass