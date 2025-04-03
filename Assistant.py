import os
import pyperclip as pc 
Quit = False

def CheckArgs(Input, Args):
    if len(Input) > Args:
        print("Too many Arguments Given")
    elif len(Input) < 1:
        print("Not Enough Arguments Given")

class Assistant:
    def __init__(self):
        self.Memory = {}
        
    def Touch(self, command):
        try:
            file = open(f"./{command[0]}", "x")
            file.close()
        except:
            print("File Already Exists")
    def Remove(self, command):
        try:
            os.remove(f"./{command[0]}")
        except:
            print("File does not exist")
    def Nano(self, command):
        try:
            subs = []
            for i in command:
                if "-" in i:
                    subs.append(i)
                    command.remove(i)
            if len(subs) == 1:
                subs = subs[0]
            print(command, command[1])
            if "\n" not in command[1]:
                command[1] += "\n"
            if os.path.isfile(f"./{command[0]}"):
                if "a" in subs:
                    user = "a"
                elif "o" in subs:
                    user = "o"
                else:
                    user = input("Do you want to overwrite or append the file (o/a)? ").lower()
                if user == "o":
                    with open(f"./{command[0]}", "w+") as f:
                        f.write(command[1])
                        f.close()
                elif user == "a":
                    with open(f"./{command[0]}", "a") as f:
                        f.write(command[1])
                        f.close()
                else:
                    print("Incorrect option")
            else:
                with open(f"./{command[0]}", "w+") as f:
                    f.write(command[1])
                    f.close()
        except:
            print("Error")
    def Read(self, command):
        with open(f"./{command[0]}", "r") as f:
            text = f.read()
            f.close()
        print(text)
    # def Copy(self, command):
    #     text = ""
    #     with open(f"./{command[0]}", "r") as f:
    #         text = f.read()
    #         f.close()
    #     pc.copy(text)
    #     print("Copied to clipboard!")

myAssis = Assistant()

while not Quit:
    user = input(">").strip().split()
    try:
        cmd = user[0].capitalize()
        getattr(myAssis, cmd)(user[1:])
    except:
        print("Command Does Not Exist")