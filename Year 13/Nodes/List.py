import Node

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node.Node(item)
        temp.set_next(self.head)
        self.head = temp

    def display(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.get_next()
myList = UnorderedList()
myList.add(1)
myList.add(4)
myList.add(3)
myList.display()
