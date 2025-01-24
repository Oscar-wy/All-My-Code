Quit = False

def CheckArgs(Input, Args):
    if len(Input) > Args:
        print("Too many Arguments Given")
    elif len(Input) < 1:
        print("Not Enough Arguments Given")

class Assistant:
    def __init__(self):
        pass
    def Touch(self, command):
        print(command)

myAssis = Assistant()

while not Quit:
    user = input(">").strip().split()
    try:
        cmd = user[0].capitalize()
        getattr(myAssis, cmd)(user[1:])
    except:
        print("Command Does Not Exist")