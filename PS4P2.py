purchasePricePerShare = float(input("Enter the purchase price per share:"))
currentStockPrice = float(input("Enter the current stock price: "))
quantityOfStock = float(input("Enter quantity of stock: "))
changeInValue = (currentStockPrice - purchasePricePerShare) * quantityOfStock
if changeInValue > 0:
    status = "increased"
elif changeInValue < 0:
    status = "decreased"
else:
    status = "no changed"
print(f"The value of the stock has {status} by ${abs(changeInValue):}")

