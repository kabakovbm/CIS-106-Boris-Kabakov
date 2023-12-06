class Employee:
  def __init__(self, employeeName, employeeSalary):
      self.employeeName = employeeName
      self.employeeSalary = employeeSalary

  def displayInfo(self):
      print(f"Name: {self.employeeName}\nSalary: ${self.employeeSalary}")

  def calculateBonus(self, bonusRate):
      bonus = self.employeeSalary * (bonusRate / 100)
      return bonus

if __name__ == "__main__":
  employee1 = Employee("Boris Kabakov", 20000)
  employee1.displayInfo()

  bonusRate = float(input("Enter the bonus rate (%): "))
  bonusAmount = employee1.calculateBonus(bonusRate)
  print(f"The bonus for {employee1.employeeName} at a rate of {bonusRate}% is: ${bonusAmount}")