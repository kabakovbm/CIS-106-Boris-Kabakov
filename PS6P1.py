
quantity = int(input("Enter the quantity of widgets: "))
if quantity > 10000:
    price = 10
elif quantity >= 5000 and quantity <= 10000:
    price = 20
else:
    price = 30

extendedPrice = quantity * price
taxRate = 0.07
taxAmount = extendedPrice * taxRate
total = extendedPrice + taxAmount
print(f"Extended Price: ${extendedPrice:.2f}")
print(f"Tax Amount: ${taxAmount:.2f}")
print(f"Total: ${total:.2f}")

