import Server.Data as Data

User = Data.User()

def Signup():
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    username = input("Enter A Username")
    if User.UsernameExists():
        print("Username Exists")
        Signup()


if __name__ == "__main__":
    Signup()