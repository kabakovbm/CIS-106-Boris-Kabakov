applianceName = input("Enter the name of the appliance: ")
applianceCost = float(input("Enter the cost of the appliance: "))
warrantyCost = 0.1 * applianceCost if applianceCost > 1000 else 0.05 * applianceCost

totalCost = applianceCost + warrantyCost

print("Appliance Name:    {}".format(applianceName))
print("Appliance Cost:    ${:.2f}".format(applianceCost))
print("Warranty Cost:     ${:.2f}".format(warrantyCost))
print("Total Cost:        ${:.2f}".format(totalCost))
