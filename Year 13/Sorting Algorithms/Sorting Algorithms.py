def bubbleSort(sortList):
	sorted = False
	length = len(sortList)
	while not sorted:
		sorted = True
		for i in range(length - 1):
			if sortList[i] > sortList[i+1]:
				temp = sortList[i]
				sortList[i] = sortList[i+1]
				sortList[i+1] = temp
				sorted = False

	return sortList

def mergeSort(sortList):
	mid = len(sortList) // 2
	leftHalf = sortList[:mid]
	rightHalf = sortList[mid:]
	if len(sortList) > 1:
		mergeSort(leftHalf)
		mergeSort(rightHalf)

def getList():
	numList = []
	while True:
		print("Add an integer number to the list: ")
		num = input()
		if num == None or num == "":
			break
		elif num[0] == "[":
			nums = num[1:-1].split(",")
			for i in nums:
				numList.append(int(i))
			break
		try:
			numList.append(int(num))
		except:
			print("Enter a integer")
	return numList

print("Bubble sort given:")
numList = getList()
print(numList)
print("Bubble sort returns")
print(bubbleSort(numList))
input()
