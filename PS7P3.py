
continueProgram = "Yes"
studentCount = 0

while continueProgram == "Yes":
    continueProgram = input("Do you want to continue? (Yes/No): ")
    if continueProgram != "Yes":
        break
    totalScore = 0
  
    lastName = input("Enter last name: ")
    examScore1 = float(input("Enter the first exam score: "))
    examScore2 = float(input("Enter the second exam score: "))
    averageScore = (examScore1 + examScore2) / 2
    print("Last Name:", lastName)
    print("Average Exam Score:", averageScore)
    studentCount = studentCount + 1
    continueProgram = input("Do you want to continue this loop? (Yes/No):")
print("Number of students who entered data:", studentCount)