from monster import Monster

class Player(Monster):
    def __init__(self, monsterName, damageRange, health):
        super().__init__(monsterName, damageRange, health)
        self.type = "Player"
        self.defending = False
    
    def defend(self):
        self.defending = not self.defending

    def subtractHp(self, hp):
        if not self.defending:
            return super().subtractHp(hp)