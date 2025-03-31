Grid = []
for i in range(3):
    Row = input()
    Grid.append(Row)
print(Grid)
Real = []
for i in Grid:
    Correct = []
    j = i.split(" ")
    for k in j:
        Correct.append(int(k))
    Real.append(Correct)
print(Real)

MagicRowCol = True
for Row in range(len(Real)):
    tot1 = 0
    tot2 = 0
    for i in range(len(Real[Row])):
        tot1 += Real[Row][i]
        tot2 += Real[i][Row]
    if tot1 != 15:
        MagicRowCol = False
    if tot2 != 15:
        MagicRowCol = False

def CheckDiag(Real):
    Total = 0
    Total2 = 0
    for i in range(len(Real)):
        for j in range(len(Real[i])):
            if i == j:
                Total += Real[i][j]
            if i + j == 2:
                Total2 += Real[i][j]
        return True

if MagicRowCol:
    if CheckDiag(Real):
        print("magic")
else:
    print("muggle")