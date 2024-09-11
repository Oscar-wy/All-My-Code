Data = [[3.2, 4.1, 1.6, 2.1, 1.6], [1.2, 2.4, 1.7, 1.9, 2.0], [7.4, 9.1, 0.5, 6.2, 3.4], [3.7, 6.2, 5.7, 4.2, 4.0]]
totall = 0
total = 0
totalflights = 0

for i in range(len(Data)):
    for j in range(len(Data[i])):
        total += Data[i][j]
        totalflights += 1
    avg = round(total / len(Data[i]), 2)
    print(f"The Mean Average Flight For Plane {i+1} Is {avg}")
    totall += total
    total = 0
avg = round(totall / totalflights, 2)
print(f"The Mean Average Distance Is {avg}")