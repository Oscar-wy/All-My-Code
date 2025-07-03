from monster import Monster

class Player(Monster):
    def __init__(self, monsterName, damageRange, health):
        super().__init__(monsterName, damageRange, health)
        self.type = "Player"
        self.defending = False
    
    def defend(self):
        self.defending = True

    def subtractHp(self, hp):
        print(self.defending)
        if not self.defending:
            self.defend()
            self.health -= hp