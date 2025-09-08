class Queue:
    def __init__(self, maxSize):
        self.Size = 0
        self.maxSize = maxSize
        self.Front = 0
        self.Rear = 0
        self.Queue = ['' for i in range(maxSize)]
        
    def enQueue(self, data):
        if self.isFull():
            return "List Full"
        print(self.Rear)
        self.Queue[self.Rear] = data
        self.Rear = (self.Rear + 1) % self.maxSize
        self.Size += 1
        return data
        
    def deQueue(self):
        if self.isEmpty():
            return "Empty List."
        data = self.Queue[self.Front]
        self.Queue[self.Front] = ''
        self.Front = (self.Front + 1) % self.maxSize
        self.Size -= 1
        return data
    
    def isFull(self):
        if self.Size == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.Size == 0:
            return True
        else:
            return False
    
    def viewQueue(self):
        if self.isEmpty():
            return []
        if self.Front < self.Rear:
            return self.Queue[self.Front:self.Rear]
        else:
            # Wrap around case: from Front to end, then from start to Rear
            return self.Queue[self.Front:] + self.Queue[:self.Rear]
    
myQueue = Queue(int(input("max size>")))
go=True
while go:
    print("1 - EnQueue")
    print("2 - DeQueue")
    print("3 - View Queue")
    print("4 - Leave")
    option=""
    try:
        option = int(input(">"))
    except:
        option=""
    if option == 1:
        print(myQueue.enQueue(input(">")))
    elif option == 2:
        print(myQueue.deQueue())
    elif option == 3:
        print(myQueue.viewQueue())
        print(f"(Front={myQueue.Front}, Rear={myQueue.Rear}, Size={myQueue.Size})")
    elif option == 4:
        go=False
    else:
        print("No command.")