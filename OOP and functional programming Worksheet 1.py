# =============== TASK 1 =============== #
# def feed(state, size):
#     size = size + 1
#     print("Fish fed")
#     if size == 5:
#         state = "FISH"

# thisFishState = "Fish"
# thisFishSize = 1
# print(f"{thisFishState} is of size {thisFishSize}")
# while thisFishState != "FISH":
#     feed(thisFishState, thisFishSize)
# print(f"It is now a big {thisFishState}")

# =============== TASK 2 =============== #
# class Animal:
#     def __init__(self, s, n):
#         self._size = s
#         self._state = n
#     def feed(self):
#         self.size += 1
#         if self.size == 5:
#             self.state = self.state.upper()
#     def getState(self):
#         return self._state
#     def getSize(self):
#         return self._size

# ============= TASK 3 ================= #

# fish = Animal(1, "fish")
# print(fish.getState())
# print(f"is of size {fish.getSize()}")

# while fish.getState() != "FISH":
#     fish.feed()
# print(f"It is now a big {fish.getState()}")

class Car:
    def __init__(self, reg, make, doi):
        self._registration = reg
        self._make = make
        self._mileage = 0
        self._dateOfInspection = doi

    def getRegistration(self):
        return self._registration
    def getMake(self):
        return self._make
    def getMileage(self):
        return self._mileage
    def getDateOfInspection(self):
        return self._dateOfInspection
    
    def setInspectionData(self, mileage, doi):
        self._mileage = mileage
        self._dateOfInspection = doi

myCar = Car("CHF1 28F", "BYD", "01/01/2025")
print(f"\n\nDetails of your car: \nMake: {myCar.getMake()}, \nRegistration: {myCar.getRegistration()}, \nMileage: {myCar.getMileage()}, \nDOI: {myCar.getDateOfInspection()}")
myCar.setInspectionData(100, "18/06/2025")
print(f"\n\nNew Inspection Info: \nMake: {myCar.getMake()}, \nRegistration: {myCar.getRegistration()}, \nMileage: {myCar.getMileage()}, \nDOI: {myCar.getDateOfInspection()}")
