exam1Score = float(input("Enter the score for the first exam: "))
exam2Score = float(input("Enter the score for the second exam: "))
weight1Exam = 0.6
weight2Exam = 0.4
totalScore = (exam1Score * weight1Exam) + (exam2Score * weight2Exam)
print(f"Total score:{totalScore}")