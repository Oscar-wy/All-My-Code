newList = input()
newList = newList.split(",")
notFit = 0
total = 0
for i in range(len(newList)):
    Pairs = newList[i].split(" ")
    if total > 0:
        total -= int(Pairs[0])
    print(total)
    if total + int(Pairs[1]) > 8:
        current = (total + int(Pairs[1])) - 8
        notFit += current
        total = 8
    else:
        total += int(Pairs[1])
print(notFit)