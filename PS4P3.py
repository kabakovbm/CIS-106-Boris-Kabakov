mealCost = float(input("Enter the total for a meal: "))

tipPercentages = [15, 18, 20]

for percentage in tipPercentages:
    tip = mealCost * (percentage / 100)
    totalWithTip = mealCost + tip
    
    print("\nWith {}% Tip:".format(percentage))
    print("Total:               {:.2f}".format(mealCost))
    print("Tip:                 {:.2f}".format(tip))
    print("Total with Tip: {:.2f}".format(totalWithTip))