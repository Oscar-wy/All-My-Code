def CreatePattern(start, end):
    index = 0
    stri = ""
    for i in range(start, end+1):
        index += 1
        stri += str(start+index)
    print(stri)
    reqd = int(input("Enter position: "))
    print(stri[reqd+1])
    FindPattern(stri)

def FindPattern(pattern):
    seen = 0
    patternLen = len(pattern)
    for i in range(patternLen):
        if i >= 101:
            break
        print(pattern[i])
        if pattern[i] == "5":
            seen += 1
    print(seen)

start = int(input(">"))
end = int(input(">"))
stri = CreatePattern(start, end)