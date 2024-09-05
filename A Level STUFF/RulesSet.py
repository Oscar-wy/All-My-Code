examScore = int(input("Enter Your Exam Score: "))
attendenceScore = int(input("Enter Your Attendence: "))
Scores = [70, 80, 90]
Grades = ["F", "C", "B", "A"]
Grade = 0
for i in range(len(Scores)):
    if examScore >= Scores[i]:
        Grade = i+1
if attendenceScore > 90:
    print(Grades[Grade])
else:
    print("Bad Attendence, Grade ", Grades[Grade])