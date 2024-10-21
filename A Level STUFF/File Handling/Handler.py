contents = ""
def readFile(text):
    try:
        with open(text+".txt", "r") as file:
            for i in file:
                data = i.split(",")
                if data[2] == "Musician\n":
                    print(data[0], data[1])
            file.close()
    except:
        print("Error, No File Found")
readFile(input(">"))
