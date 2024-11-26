def CreatePattern(start, end):
    stri = []
    for i in range(start, end+1):
        stri.append(str(i))
    print(stri)
    return stri

def FindPattern(pattern, rs):
    patternLen = len(pattern)
    for i in range(patternLen):
        if pattern[i] == rs:
            print(i, pattern[i])

start = int(input(">"))
end = int(input(">"))
stri = CreatePattern(start, end)
FindPattern(stri, 999)