total = 0
n = 10
for student in range(1, n):
    for mark in range(1, 3):
        total = total + results[student][mark]
for student in range(1, n):
    average[student] = (mark[1] + mark[2] + mark[3]) / 3

