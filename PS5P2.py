item = input("Enter the item (A or any other letter for B): ")
quantity = int(input("Enter the quantity: "))

unitPrice = 10.0 if item == "A" else 20.0

extendedPrice = quantity * unitPrice

print("Item:          {}".format(item))
print("Unit price:    ${:.2f}".format(unitPrice))
print("Extended price: ${:.2f}".format(extendedPrice))