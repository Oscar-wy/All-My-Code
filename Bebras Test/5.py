all = input()
all = all.split()
posts = int(all[0])
railings = int(all[1])
pickets = int(all[2])
posts = posts - 1
length = 0
for i in range(posts):
    canPicket = False
    if railings - 2 >= 0:
        railings -= 2
        canPicket = True
    if canPicket:
        if pickets - 8 >= 0:
            pickets -= 8
            length += 2
print(length)