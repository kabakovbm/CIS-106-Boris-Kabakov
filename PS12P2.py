def displayStudentInfo(names, scores):
  for i in range(len(names)):
      print(f"Name: {names[i]}, Score: {scores[i]}")

def displayStudentInfoReverse(names, scores):
  for i in range(len(names)-1, -1, -1):
      print(f"Name: {names[i]}, Score: {scores[i]}")

lastNames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
examScores = [85, 90, 78, 92, 88, 76, 94, 89, 82, 95]

print("Original Order:")
displayStudentInfo(lastNames, examScores)

print("\nReverse Order:")
displayStudentInfoReverse(lastNames, examScores)