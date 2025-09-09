def enqueue(item):
    global queue
    global backofqueue
    for i in range(0, backofqueue):
        if queue[i][1] <= item[1]:
            lowestindex = i

    # queue[backofqueue]=item
    # backofqueue=backofqueue+1


def dequeue():
    global queue
    global backofqueue
    highest = 0
    highestindex = 0
    for i in range(0, backofqueue):
        if queue[i][1] > highest:
            highest=queue[i][0]
            highestindex = i
    out=queue[highestindex][0]
    for i in range(highestindex, backofqueue-1):
        queue[i]=queue[i+1]
    backofqueue-=1
    queue[backofqueue]=""
    return out
    #find the highest priority in the queue and return it, update queue   
    
    

    
#items stored as tuples
#second value is priority in this example bigger number is more important
#in an real array blank values would need to be tuples too...
queue=[("bob",1),("James",1),"","","","","","","",""]
backofqueue=2
go=True

while (go):
    print("Queue example")
    print("Enter 1 to Enqueue")
    print("Enter 2 to Dequeue")
    print("Enter 3 to see the state of the whole queue")
    print("any other key to exit")

    choice =input()

    if choice=="1":
        if backofqueue==10:
            print("Queue full")
        else:
            value = input("data >")
            priority = input(input("prio > "))
            myTuple = (value, priority)
            enqueue(myTuple)
            # get value and priority data
            # pack into tuple
            # put in queue

    elif choice=="2":
        if backofqueue==0:
            print("empty queue, nothing to dequeue")
        else:
            print(dequeue())
        
    elif choice=="3":
        print(queue)
        
    else:
        go=False
        

