
principal = float(input("Enter the principal amount: "))
yearsToMaturity = int(input("Enter the years to maturity: "))


if principal > 100000:
    interestRate = 0.06
elif 50000 <= principal <= 100000:
   interestRate = 0.05 if yearsToMaturity == 10 else 0.04
else:
    interestRate = 0.02


firstYearInterest = principal * interestRate


print("Principal Amount:", principal)
print("Interest Rate:", interestRate * 100, "%")
print("Interest Amount for the First Year:", firstYearInterest)