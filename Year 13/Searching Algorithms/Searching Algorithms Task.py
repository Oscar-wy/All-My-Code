import random
x = 10

def getVal():
	value = int(input("Give number: "))
	return value

def generateList():
	length = int(input("Enter length of list"))
	generatedList = [i for i in range(length+1)]
	return generatedList

def linearSearch(searchList, searchVal):
	ctr = 0
	for index, i in enumerate(searchList):
		ctr += 1
		if i == searchVal:
			return index, f"Amount Taken {ctr}"
	return ("Value not found")

def binarySearch(searchList, searchVal):
	start = 0
	end = len(searchList) - 1
	ctr = 0
	while start <= end:
		ctr += 1
		mid = (start + end) // 2
		if searchList[mid] == searchVal:
			return mid, f"Amount taken {ctr}"
		elif searchList[mid] < searchVal:
			start = mid + 1
		elif searchList[mid] > searchVal:
			end = mid + 1
	return ("Value not found")

def recursiveBinarySearch(searchList, searchVal, start=0, end=None):
	if end == None:
		end = len(searchList) - 1
	mid = round((start + end) // 2)
	if searchList[mid] == searchVal:
		return mid, searchVal
	elif searchList[mid] < searchVal:
		start = mid + 1
		return recursiveBinarySearch(searchList, searchVal, start, end)
	elif searchList[mid] > searchVal:
		end = mid + 1
		return recursiveBinarySearch(searchList, searchVal, start, end)
	else:
		return ("Value not found")

searchList = generateList()
print(searchList)
x = getVal()
print(linearSearch(searchList, x))
print(binarySearch(searchList, x))
print(recursiveBinarySearch(searchList, x))
input()

def test():
	amountOfTests = 5
	testAmount = 1000
	listSize = 1
	myComparisons = {}
	for i in range(amountOfTests):
		ctr = 0
		listSize = listSize * 10
		myList = [i for i in range(listSize+1)]
		binaryAvg = 0
		linearAvg = 0
		binaryTotal = 0
		linearTotal = 0
		while ctr < testAmount:
			myNum = random.randint(0, listSize)
			linearTotal += linearSearch(myList, myNum)[0]
			binaryTotal += binarySearch(myList, myNum)[0]
		binaryAvg = binaryTotal / testAmount
		linearAvg = linearTotal / testAmount
		myComparisons[listSize] = [f"Binary Avg: {binaryAvg}", f"Linear Avg: {linearAvg}"]
	print(myComparisons)

test()