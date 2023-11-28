def displayStudentInfo(names, scores):
  for i in range(len(names)):
      print(f"Name: {names[i]}, Score: {scores[i]}")

def displayStudentInfoReverse(names, scores):
  for i in range(len(names)-1, -1, -1):
      print(f"Name: {names[i]}, Score: {scores[i]}")

def displayHighestLowest(names, scores):
  highVar = 0
  lowVar = 999
  highIndex = 0
  lowIndex = 0

  for i in range(len(scores)):
      if scores[i] > highVar:
          highVar = scores[i]
          highIndex = i
      if scores[i] < lowVar:
          lowVar = scores[i]
          lowIndex = i

  print(f"\nHighest Score: Name - {names[highIndex]}, Score - {highVar}")
  print(f"Lowest Score: Name - {names[lowIndex]}, Score - {lowVar}")

with open("data.txt", "r") as file:
  lines = file.readlines()

lastNames = []
examScores = []

for line in lines:
  data = line.strip().split(',')
  lastNames.append(data[0])
  examScores.append(int(data[1]))

print("Original Order:")
displayStudentInfo(lastNames, examScores)

print("\nReverse Order:")
displayStudentInfoReverse(lastNames, examScores)

displayHighestLowest(lastNames, examScores)