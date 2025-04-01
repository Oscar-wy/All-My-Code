rice = int(input())
curRice = rice
ctr = 0
num = 1
canPut = True
while canPut == True:
    num = num * 2
    if num > curRice:
        canPut = False
    else:
        curRice - num
        ctr += 1

print(ctr)