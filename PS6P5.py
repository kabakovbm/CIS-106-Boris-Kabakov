
lastName = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
jobLevel = int(input("Enter employee job level: "))

if jobLevel >= 10:
  bonusRate = 0.25  
elif 5 <= jobLevel <= 9:
  bonusRate= 0.20  
else:
  bonusRate = 0.10 


bonus = salary * bonusRate

print(f"Employee last name: {lastName}")
print(f"Bonus: ${bonus:.2f}")