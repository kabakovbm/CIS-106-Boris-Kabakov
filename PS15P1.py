class Employee:
  def __init__(self, employeeName, employeeSalary):
      self.employeeName = employeeName
      self.employeeSalary = employeeSalary

  def displayInfo(self):
      print(f"Name: {self.employeeName}\nSalary: ${self.employeeSalary}")

  def calculateBonus(self, bonusRate):
      bonus = self.employeeSalary * (bonusRate / 100)
      return bonus


class Manager(Employee):
  def longTermBonus(self):
      return 0.4 * self.employeeSalary


if __name__ == "__main__":
  employee1 = Employee("Boris Kabakov", 20000)
  employee1.displayInfo()

 
  bonusRate = float(input("Enter the bonus rate (%): "))
  bonusAmount = employee1.calculateBonus(bonusRate)
  print(f"The bonus for {employee1.employeeName} at a rate of {bonusRate}% is: ${bonusAmount}")

  manager1 = Manager("Boris Kabakov", 20000)
  manager1.displayInfo()

  longTermBonusAmount = manager1.longTermBonus()
  print(f"The long-term bonus for {manager1.employeeName} is: ${longTermBonusAmount}")
