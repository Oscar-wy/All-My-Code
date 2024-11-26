def RunList(n):
    stri = ""
    for i in range(0, 2^59):
        stri += str(n+i)
    print(stri)


RunList(1000)