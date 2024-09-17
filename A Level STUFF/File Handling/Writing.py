# fName = input("Enter Your First Name: ")
# lName = input("Enter Your Last Name: ")
# dateOfBirth = input("Enter Your Date of Birth: ")
with open("newFile.txt", "w") as file:
    for i in range(5):
        name = input("Enter A Name: ")
        file.write(name+"\n")
    file.close()