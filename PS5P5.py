lastName = input("Enter your last name: ")
numDependents = int(input("Enter the number of dependents: "))
grossIncome = float(input("Enter your gross income: "))

adjustedGrossIncome = grossIncome - (numDependents * 12000)

taxRate = 0.2 if adjustedGrossIncome > 50000 else 0.1

incomeTax = adjustedGrossIncome * taxRate

if incomeTax < 100:
    incomeTax = 100

print("Last Name:           {}".format(lastName))
print("Gross Income:        ${:.2f}".format(grossIncome))
print("Number of Dependents: {}".format(numDependents))
print("Adjusted Gross Income: ${:.2f}".format(adjustedGrossIncome))
print("Income Tax:          ${:.2f}".format(incomeTax))
