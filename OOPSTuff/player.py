from monster import Monster

class Player(Monster):
    def __init__(self, monsterName, damageRange, health):
        super().__init__(monsterName, damageRange, health)
        