def mypop():
    global stack
    global topofstack
    topofstack -= 1
    temp = stack[topofstack]
    stack[topofstack] = ""
    return temp
    #pop should remove and return the value top of the stack and update the topofstack value

    
    
def mypush(item):
    global stack
    global topofstack
    stack[topofstack] = item
    topofstack += 1
    return item
    #push should change put item and the top of the stack and update topofstack


stack=["bob","James","","","","","","","",""]
topofstack=2
go=True

while (go):
    print("Stack example")
    print("Enter 1 to push")
    print("Enter 2 to pop")
    print("Enter 3 to see the state of the whole stack")
    print("any other key to exit")

    choice =input()

    if choice=="1":
        data = input("data > ")
        if len(stack) != topofstack:
            print(mypush(data))
        else:
            print("Stack is full.")
        #get the data to push and push it
        #error handling needed

    elif choice=="2":
        print(mypop())
        #print the value that has been popped
        #error handling needed
        
    elif choice=="3":
        print(stack)
        
    else:
        go=False
        

