def displayNames(names):
  for name in names:
      print(name)

def displayNamesReverse(names):
  for name in reversed(names):
      print(name)

lastNames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

print("Original Order:")
displayNames(lastNames)

print("\nReverse Order:")
displayNamesReverse(lastNames)
