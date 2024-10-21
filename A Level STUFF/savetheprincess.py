from random import randint

size=2
while size%2==0:
    size=int(input("enter the grid size - must be an odd number: "))

grid=[["-" for x in range(size)] for y in range(size)]
mid=(size//2)
grid[mid][mid]="m"
grid[randint(0,size-1)][randint(0,size-1)]="p"

for row in grid:
    for e in row:
        print (e, end='')
    print()

print("Maurizio needs to rescue the Princess")

maurCoords = []
prinCoords = []

for i in range(len(grid)):
    print(grid[i])
    for j in range(len(grid[i])):
        if grid[i][j] == "p":
            prinCoords = [i, j]
        if grid[i][j] == "m":
            maurCoords = [i, j]

if maurCoords[0] > prinCoords[0]:
    coordValue = maurCoords[0] - prinCoords[0]
    for i in range(coordValue):
        print("UP")
else:
    coordValue = prinCoords[0] - maurCoords[0]
    for i in range(coordValue):
        print("DOWN")

if maurCoords[1] > prinCoords[1]:
    coordValue = maurCoords[1] - prinCoords[1]
    for i in range(coordValue):
        print("LEFT")
else:
    coordValue = prinCoords[1] - maurCoords[1]
    for i in range(coordValue):
        print("RIGHT")


#you need to write the code to solve the puzzle
# It should output the directions Maurizio needs to take to get to Princess Pineapple
# Directions should be output in the form "UP" "DOWN" "LEFT" "RIGHT"
# e.g. "UP" "UP" "LEFT" "LEFT" "LEFT"


#hints

# use nested for loops to find the princesses row and column
# calculate the difference between that co-ordinate and Maurizio
# output the correct command set
