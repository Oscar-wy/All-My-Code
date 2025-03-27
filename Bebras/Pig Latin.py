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
for Row in range(Real):
    tot1 = 0
    tot2 = 0
    for i in Real[Row]:
        tot1 += Real[Row][i]
        tot2 += Real[i][Row]
    if tot1 != 15:
        MagicRowCol = False
    if tot2 != 15:
        MagicRowCol = False

def CheckDiag(Real):
    Total = 0
    for i in range(Real):
        for j in range(Real[i]):
            if i == j:
                Tot1 += Real[i][j]
                Tot2 += Real[3-i][j]

if MagicRowCol:
    CheckDiag(Real)
else:
    print("Muggle")