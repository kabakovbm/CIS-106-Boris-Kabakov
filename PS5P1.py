quantity = int(input("Enter the quantity of the item: "))

unitPrice = 3.0 if quantity >= 1000 else 5.0

extendedPrice = quantity * unitPrice

tax = 0.07 * extendedPrice

total = extendedPrice + tax

print("Quantity:      {}".format(quantity))
print("Unit price:    ${:.2f}".format(unitPrice))
print("Extended price: ${:.2f}".format(extendedPrice))
print("Tax (7%):      ${:.2f}".format(tax))
print("Total:          ${:.2f}".format(total))