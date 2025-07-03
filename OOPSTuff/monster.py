import random
from item import Item

class Monster:
    def __init__(self, name, damageRange, health):
        self.name = name
        self.health = health
        self.damageRange = damageRange
        self.type = "Monster"
        self.weapon = None
        self.loot = Item("Flesh", "Bloody Flesh From Zombie", 0)
    def __repr__(self):
        return f"This is the {self.type} class with the name: {self.name}"
    def giveWeapon(self, weapon):
        self.weapon = weapon
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def describe(self):
        if self.health >= 90:
            return "You are very healthy"
        elif self.health >= 50:
            return "You are moderately healthy"
        elif self.health < 50 and self.health > 20:
            return "You are unwell"
        elif self.health < 20 and self.health > 1:
            return "You are very unwell"
        else:
            return "You are dead!"
    def isAlive(self):
        if self.health > 0:
            return True
        return False
    def subtractHp(self, hp):
        self.health -= hp
    def getDamageAttack(self):
        return random.randint(self.damageRange[0], self.damageRange[1])
    def attack(self, target):
        if target.defending == True:
            print(target.defending)
            defendchance = random.randint(1, 10)
            if defendchance == 1:
                if self.weapon != None:
                    damage = self.weapon.get_attack_value()
                    target.subtractHp(damage)
                    print(f">>> {self.name} damages {target.name} for {damage} HP")
        else:
            damage = self.weapon.get_attack_value()
            target.subtractHp(damage)
            print(f">>> {self.name} damages {target.name} for {damage} HP")
        target.defending = False
    def getHealth(self):
        return self.health
    def getLoot(self):
        return self.loot