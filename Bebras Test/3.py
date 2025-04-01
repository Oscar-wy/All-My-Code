cards = input()
cards = cards.split(" ")
GiveCards = ""
card = 0
for i in range(13):
    GiveCards += f" {cards[card]}"
    card += 4
print(GiveCards)