class OOPCourse:
    def __init__(self):
        
    def Age(self, age):
        self.age = age
    def SetName(self, name):
        self.name = name
    def welcome(self):
        print(f"Hello, {self.name}, Welcome to object-oriented programming")
    def agestring(self):
        print(f"You are, {self.age}, years old")

Person1 = OOPCourse()
Person2 = OOPCourse()

Person1.SetName("James")
Person1.welcome()
Person1.Age(17)
Person1.agestring()

Person2.SetName("Kevin")
Person2.welcome()
Person2.Age(0)#Mental age
Person2.agestring()

