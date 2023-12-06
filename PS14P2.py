class Student:
  def __init__(self, firstName, lastName, districtCode, enrolledCredits):
      self.firstName = firstName
      self.lastName = lastName
      self.districtCode = districtCode
      self.enrolledCredits = enrolledCredits

  def computeTuition(self):
      inDistrictRate = 250.00
      outOfDistrictRate = 500.00

      if self.districtCode == 'I':
          tuitionRate = inDistrictRate
      else:
          tuitionRate = outOfDistrictRate

      tuitionOwed = self.enrolledCredits * tuitionRate
      return tuitionOwed


if __name__ == "__main__":
  student1 = Student("Boris", "Kabakov", "I", 16)

  print("Student Information:")
  print(f"Name: {student1.firstName} {student1.lastName}")
  print(f"District Code: {student1.districtCode}")
  print(f"Enrolled Credits: {student1.enrolledCredits}")

  tuitionAmount = student1.computeTuition()
  print(f"Tuition Owed: ${tuitionAmount}")
