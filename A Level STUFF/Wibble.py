# def Wibbler(n):
#     if n > 0:
#         print("Wibble")
#         return Wibbler(n-1)

# Wibbler(100)

# def Wibbler(n):
#     if n == 1:
#         return("Wibble")
#     return("Wibble" + Wibbler(n-1))

# print(Wibbler(3))

def allStar(n):
    if len(n) == 1:
        return n
    print(n[1:])
    return n[0]+"*" + allStar(n[1:])


print(allStar("Hello"))