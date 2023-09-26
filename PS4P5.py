fixedCosts = float(input("Enter the fixed costs: $"))
pricePerUnit = float(input("Enter the price per unit: $"))
costPerUnit = float(input("Enter the cost per unit: $"))

breakEvenPoint = fixedCosts / (pricePerUnit - costPerUnit)

print(f"To break even, you need to sell {breakEvenPoint:.2f} units.")

