def SumOfAllEven(num):
    print(num)
    if num <= 0:
        return num
    elif num % 2 == 0:
        return num + SumOfAllEven(num-2)
    else:
        return SumOfAllEven(num-1)
    
print(SumOfAllEven(10))