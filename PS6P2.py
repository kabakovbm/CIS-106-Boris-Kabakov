
partNumber = input("Enter the part number: ")
quantity = int(input("Enter the quantity: "))


if partNumber == "10" or partNumber == 55:
    unitCost = 1.00
elif partNumber == 99:
    unitCost = 2.00
elif partNumber == "80" or partNumber == "70":
    unitCost = 3.00
else:
    unitCost = 5.00

totalCost = quantity * unitCost
print("Part Number: ", partNumber)
print("Cost Per Unit: ", unitCost)
print("Total Cost: ", totalCost)