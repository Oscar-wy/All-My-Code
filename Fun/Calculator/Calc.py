def Main():
    print("Enter Calculation, 'X' to stop")
    user = input(">")
    if user.lower() == "x":
        exit()
    calc = user.strip()
    print(calc)
    calc += "="
    nums = {}
    Operators = []
    num = ""
    ctr = 0
    for i in range(len(calc)):
        if calc[i].isnumeric():
            num += calc[i]
            print(num)
        else:
            nums[ctr] = int(num)
            num = ""
            ctr += 1
    print(nums)
    calc = list(calc)
    lencalc = len(calc)
    opCtr = 0
    for i in range(len(calc)):
        print(i)
        if calc[i] == "x" or calc[i] == "*":
            Operators.append(["Mul", opCtr])
            calc[i] = " "
            opCtr += 1
        elif calc[i] == "/" or calc[i] == "÷":
            Operators.append(["Div", opCtr])
            calc[i] = " "
            opCtr += 1
        elif calc[i] == "+":
            Operators.append(["Plus", opCtr])
            calc[i] = " "
            opCtr += 1
        elif calc[i] == "-":
            Operators.append(["Min", opCtr])
            calc[i] = " "
            opCtr += 1
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
            print(Operator[1])
            print(nums)
            print(nums[Operator[1]])
            num = nums[Operator[1]] * nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1])
            if Operator[1] > 0:
                nums[Operator[1]] = num
            else:
                nums[Operator[1]+1] = num
        elif Operator[0] == "Div":
            num = nums[Operator[1]] / nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1])
            if Operator[1]-1 != 0:
                nums[Operator[1]] = num
            else:
                nums[Operator[1]+1] = num
        elif Operator[0] == "Plus":
            num = nums[Operator[1]] + nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1])
            if Operator[1]-1 != 0:
                nums[Operator[1]] = num
            else:
                nums[Operator[1]+1] = num
        elif Operator[0] == "Min":
            num = nums[Operator[1]] - nums[Operator[1]+1]
            nums.pop(Operator[1]+1)
            nums.pop(Operator[1])
            if Operator[1]-1 != 0:
                nums[Operator[1]] = num
            else:
                nums[Operator[1]+1] = num
    print(num)



Main()