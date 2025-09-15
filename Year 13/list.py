import random
#myList = [random.randint(0, 100) for i in range(50)]
myList = range(1, 100)
print(myList)
num = 7

def LinearSearch():
    for i in range(len(myList)):
        if myList[i] == num:
            return "Found Number"
    return "Number Not In List"

def BinarySearch():
    currList = myList
    Found = False
    while Found != True:
        if len(currList) >= 2:
            print(currList)
            currIndex = round(len(currList)/2)
            if currList[currIndex] == num:
                Found = True
            elif currList[currIndex] <= num:
                currList = currList[currIndex:len(currList)]
            else:
                currList = currList[0:currIndex]
        else:
            return "Not Found"
    return "Found"

print(LinearSearch())
print(BinarySearch())