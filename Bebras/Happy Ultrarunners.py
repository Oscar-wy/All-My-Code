n = int(input())
happy = 0
for i in range(n):
    Runner = input()
    Runner = Runner.split(" ")
    prev = 0
    total = 0
    for i in Runner:
        if int(i) > prev:
            prev = int(i)
            total += 1
    if total == len(Runner):
        happy += 1
print(happy)