def Factorial(num):
    if num == 1:
        return num
    return num * Factorial(num-1)

print(Factorial(5))