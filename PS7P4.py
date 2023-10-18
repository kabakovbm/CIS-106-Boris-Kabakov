continueProgram = "Yes"
employeeCount = 0
totalGrossPay = 0
while continueProgram == "Yes":
    continueProgram = input("Do you want to continue? (Yes/No): ")
    if continueProgram != "Yes":
        break
    lastName = input("Enter employee last name: ")
    hoursWorked = float(input("Enter hours worked: "))
    rateOfPay = float(input("Enter rate of pay: "))
    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        grossPay = (40 * rateOfPay) + (overtimeHours * (rateOfPay * 1.5))
    else:
        grossPay = hoursWorked * rateOfPay
    print("Last Name:", lastName)
    print("Gross Pay: $", grossPay)
    totalGrossPay += grossPay
    employeeCount += 1
    continueProgram = input("Do you want to continue this loop? (Yes/No): ")
print("Sum of all gross pays: $", totalGrossPay)
print("Number of employees: ", employeeCount)
if employeeCount > 0:
    averagePay = totalGrossPay / employeeCount
    print("Average Pay: $", averagePay)
