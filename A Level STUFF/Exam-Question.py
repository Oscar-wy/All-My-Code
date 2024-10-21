Number = 0
while Number < 1 or Number > 10:
    Number = int(input("Enter A Positive Whole Number: "))
    if Number > 10:
        print("Number Too Large!")
    else:
        if Number < 1:
            print("Not A Positive Number!")
c = 1
for k in range(Number-1):
    print(c)
    c = (c * (Number - 1 - k) // (k + 1))