
# 1. Prompt the user for a number and create a list
numItems = int(input("Enter the number of items for the list: "))
myList = []

for i in range(numItems):
    num = int(input(f"Enter integer {i + 1}: "))
    myList.append(num)

print("Your list:", myList)

# 2. Insert 99 at position 1 within the list
myList.insert(0, 99)
print("Updated list after inserting 99:", myList)

# 3. Replace the value of 99 with 100
myList[myList.index(99)] = 100
print("Updated list after replacing 99 with 100:", myList)

# 4. Create a second list and extend the first list
secondList = [500, 600, 700, 800, 900]
print("Second list:", secondList)

myList.extend(secondList)
print("First list after extending with the second list:", myList)

# 5. Remove the value 800 from the first list
myList.remove(800)
print("First list after removing 800:", myList)

# 6. Remove the third item from the first list
del myList[2]
print("First list after removing the third item:", myList)

# 7. Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]

# 8. Display the count of A grades
print("Count of A grades:", grades.count("A"))

# 9. Display the index of the first B grade
print("Index of the first B grade:", grades.index("B"))

# 10. Look for grade F and display a message
if "F" not in grades:
    print("F is not in the list.")

# 11. Clear the second list without deleting
secondList.clear()
print("Cleared second list:", secondList)

# 12. Delete the second list and try to display it (should generate an error)
del secondList
# print(secondList)  # Uncommenting this line will raise an error

# 13. Create a list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14. Sort the list of players
players.sort()
print("Sorted list of players:", players)

# 15. Make a copy of the list called players2
players2 = players.copy()
print("Copy of the list (players2):", players2)

# 16. Reverse the order of players2
players2.reverse()
print("Reversed players2:", players2)