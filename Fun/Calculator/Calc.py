def Main():
    print("Enter Calculation, 'X' to stop")
    user = input(">")
    if user.lower() == "x":
        exit()
    calc = user.strip()
    calc = list(calc)
    Operators = []
    nums = {}
    for i in range(len(calc)):
        print(i)
        if calc[i] == "x" or calc[i] == "*":
            Operators.append(["Mul", i])
        elif calc[i] == "/" or calc[i] == "÷":
            Operators.append(["Div", i])
        thing = calc[i].isnumeric()
        print(thing)
        if thing:
            nums[i] = int(calc[i])
    for i in range(len(calc)):
        if calc[i] == "+":
            Operators.append(["Plus", i])
        elif calc[i] == "-":
            Operators.append(["Min", i])
    print(nums, Operators)
    for i in range(len(Operators)):
        Operator = Operators[i]
        if Operator[0] == "Mul":
            num = nums[Operator[1]-1] * nums[Operator[1]+1]
            print(num)
            nums[Operator[1]+1].pop()
        elif Operator[0] == "Div":
            num = nums[Operator[1]-1] * nums[Operator[1]+1]
            print(num)
            nums[Operator[1]+1].pop()
            num = nums[Operator[1]-1] * nums[Operator[1]+1]
            print(num)
            nums[Operator[1]+1].pop()
        elif Operator[0] == "Min":
            num = nums[Operator[1]-1] * nums[Operator[1]+1]
            print(num)
            nums[Operator[1]+1].pop()
    print(nums)



Main()