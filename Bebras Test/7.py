stacks = input()
stacks = stacks.split()
Complete = False
ctr = 1
days = 0
Done = 0
while not Complete:
    if Done == len(stacks):
        Complete = True
    if ctr+1 == len(stacks):
        ctr = 1
        days += 1
    if stacks[ctr]  < stacks[ctr-1]:
        stacks[ctr] += 1
    else:
        Done += 1
    ctr += 1
print(days)