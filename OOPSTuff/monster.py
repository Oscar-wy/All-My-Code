import random

class Monster:
    def __init__(self, monsterName, damageRange, health):
        self.name = monsterName
        self.health = health
        self.damageRange = damageRange
    def __repr__(self):
        return f"This is the monster class with the name: {self.name}"
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
        damage = self.getDamageAttack()
        target.subtractHp(damage)
        print(f">>> {self.name} damages {target.name} for {damage} HP")