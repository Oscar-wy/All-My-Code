n = input()
NumList = input()
NumList = NumList.split(" ")
for i in range(1, int(n)+1):
    if str(i) in NumList:
        NumList.remove(str(i))
    else:
        NumList.append(i)
print(NumList[0])