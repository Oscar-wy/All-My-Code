def Main():
    print("Enter Calculation, 'X' to stop")
    user = input(">")
    if user.lower() == "x":
        exit()
    calc = user.strip()
    calcLi = []
    num = ""
    for i in range(len(calc)):
        if calc[i].isnumeric():
            print(num)
            num += calc[i]
        else:
            calcLi.append(num)
            num = ""
    print("Cal", calcLi)
    calc = list(calc)
    Operators = []
    nums = {}
    lencalc = len(calc)
    for i in range(len(calc)):
        print(i)
        if calc[i] == "x" or calc[i] == "*":
            Operators.append(["Mul", i])
            calc[i] = " "
        elif calc[i] == "/" or calc[i] == "÷":
            Operators.append(["Div", i])
            calc[i] = " "
        thing = calc[i].isnumeric()
        print(thing)
        if thing:
            nums[i] = int(calc[i])
    for i in range(len(calc)):
        if calc[i] == "+":
            Operators.append(["Plus", i])
            calc[i] = " "
        elif calc[i] == "-":
            Operators.append(["Min", i])
            calc[i] = " "
    stri = ""
    for i in calc:
        stri += i
    calc = stri
    print(calc)
    calc = calc.split()
    print(calc)
    print(nums, Operators)
    for i in range(len(Operators)):
        Operator = Operators[i]
        num = 0
        if Operator[0] == "Mul":
            num = nums[Operator[1]-1] * nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1]-1)
            if Operator[1]-1 != 0:
                nums[Operator[1]-1] = num
            else:
                nums[Operator[1]+1] = num
        elif Operator[0] == "Div":
            num = nums[Operator[1]-1] / nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1]-1)
            if Operator[1]-1 != 0:
                nums[Operator[1]-1] = num
            else:
                nums[Operator[1]+1] = num
        elif Operator[0] == "Plus":
            num = nums[Operator[1]-1] + nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1]-1)
            if Operator[1]-1 != 0:
                nums[Operator[1]-1] = num
            else:
                nums[Operator[1]+1] = num
        elif Operator[0] == "Min":
            num = nums[Operator[1]-1] - nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1]-1)
            if Operator[1]-1 != 0:
                nums[Operator[1]-1] = num
            else:
                nums[Operator[1]+1] = num
    print(num)



Main()