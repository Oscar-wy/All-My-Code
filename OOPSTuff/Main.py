import random
from monster import Monster
from player import Player
you = Player("Peter", [7, 20], 100) # CREATED THE PLAYER
enemies = []
for i in range(4):
    enemies.append(Monster(f"enemy{i}", [1,5], 50))
# print(you)
# you.setName("Peter")
# print(you)
# print(you.describe())
# print(you.isAlive())
# you.subtractHp(10)
# print(you.isAlive())
enemiesDead = 0
while you.isAlive():
    for enemy in enemies:
        if enemy.isAlive():
            if you.health <= 0:
                break
            you.attack(enemy)
            defend = input(">")
            if defend.lower() == "y":
                you.defend()
            enemy.attack(you)
            if not enemy.isAlive():
                print(f"You killed {enemy.name}")
                enemiesDead += 1
            print(you.health)
    if enemiesDead == len(enemies):
        break
if you.isAlive():
    print("Well done you killed all the enemies")
else:
    print("You failed the wave!")

# while enemy.isAlive() and you.isAlive():
#     go = random.randint(0, 1)
#     if go == 1:
#         you.attack(enemy)
#     else:
#         enemy.attack(you)
# if enemy.isAlive():
#     print(f"The {enemy.name} defeated you in battle!")
# else:
#     print(f"You defeated {enemy.name}")