def CheckPalindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False

def PalindromicSum(num):
    Palindromes = []
    if CheckPalindrome(num):
        return [num]
    for i in range(num):
        currentNum = num-i
        if CheckPalindrome(currentNum):
            Palindromes.append(currentNum)
    seen = {}
    for i, number in enumerate(Palindromes):
        secnum = num - Palindromes[i]
        if secnum in seen:
            return (secnum, Palindromes[i])
        else:
            seen[number] = i
    Possible = []
    seen = {}
    for i, number in enumerate(Palindromes):
        for j, number in enumerate(Palindromes):
            secnum = num - (Palindromes[i] + Palindromes[j])
            if secnum in seen:
                Possible.append((Palindromes[i], Palindromes[j], secnum))
            else:
                seen[number] = i
    return Possible[len(Possible)-1]

def RequireThree():
    three = 0
    for i in range(1, 1000000):
        print(i)
        num = PalindromicSum(i)
        if len(num) == 3:
            three += 1
    print(three)

RequireThree()
user = int(input("Enter A Number Between 1-1,000,000: "))
print(PalindromicSum(user))