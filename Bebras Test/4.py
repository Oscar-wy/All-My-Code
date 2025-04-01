num = int(input())
largeBox = 24
smallBox = 5
amntLarge = 0
amntSmall = 0
Complete = False
while not Complete:
    if num - largeBox < 0:
        if num - smallBox < 0:
            num -= num
            amntSmall += 1
            Complete = True
        else:
            num -= smallBox
            amntSmall += 1
    else:
        num -= largeBox
        amntLarge += 1
print(amntLarge, amntSmall)