from monster import Monster

class Player(Monster):
    def __init__(self, monsterName, damageRange, health):
        super().__init__(monsterName, damageRange, health)
        self.type = "Player"
        self.defending = False
        self.items = []
    
    def defend(self):
        self.defending = True

    def subtractHp(self, hp):
        print(self.defending)
        if not self.defending:
            self.defend()
            self.health -= hp

    def attack(self, target):
        damage = self.getDamageAttack()
        enemHealth = target.health - damage
        if enemHealth <= 0:
            self.items.append(target.getLoot())
        target.subtractHp(damage)
        print(f">>> {self.name} damages {target.name} for {damage} HP")