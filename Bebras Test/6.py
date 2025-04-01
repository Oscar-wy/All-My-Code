swimmers = input()
swimmers = swimmers.split(" ")
curFastestSwimmer = 0
Ranks = ""
curRank = 0
for i in range(len(swimmers)):
    currentSwimmer = int(swimmers[i])
    if currentSwimmer < curFastestSwimmer + 10:
        Ranks += f"{curRank} "
    else:
        curFastestSwimmer = currentSwimmer
        curRank = i+1
        Ranks += f"{curRank} "
print(Ranks)

