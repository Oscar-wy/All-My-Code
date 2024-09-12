set = []
def Big(*args):
    for i in range(len(args)):
        set.append(args[i])
    set.sort()
    return f"{set[len(set) - 1]} Is The Biggest"
    
a = int(input(">"))
b = int(input(">"))
c = int(input(">"))
print(Big(a, b, c))