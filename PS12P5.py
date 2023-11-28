def displayPlayerInfo(names, averages):
  for i in range(len(names)):
      print(f"Player: {names[i]}, Batting Average: {averages[i]}")

def searchPlayer(names, averages, search_name):
  for i in range(len(names)):
      if names[i] == search_name:
          print(f"Player found: {names[i]}, Batting Average: {averages[i]}")
          return True
  print(f"Name not found: {search_name}")
  return False


with open("data.txt", "r") as file:
  lines = file.readlines()

playerNames = []
battingAverages = []

for line in lines:
  data = line.strip().split(',')
  playerNames.append(data[0])
  battingAverages.append(float(data[1]))


print("Player Information:")
displayPlayerInfo(playerNames, battingAverages)


while True:
  searchName = input("\nEnter a last name to search (or type 'exit' to end): ").capitalize()

  if searchName.lower() == 'exit':
      break

  searchPlayer(playerNames, battingAverages, searchName)
