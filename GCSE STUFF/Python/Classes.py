class MyClass():
    def __init__(self, *List):
        for i in range(len(List)):
            self.name = List[i]

p1 = MyClass("Data1", "Data2")
