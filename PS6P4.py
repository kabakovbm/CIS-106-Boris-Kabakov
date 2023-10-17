numTickets = int(input("Enter the number of concert tickets: "))

if numTickets >= 25:
    pricePerTicket = 50
elif numTickets >= 10:
  pricePerTicket = 60
elif numTickets >= 5:
  pricePerTicket = 70
else:
  pricePerTicket = 75

totalCost = numTickets * pricePerTicket

print(f"Number of tickets: {numTickets}")
print(f"Price per ticket: ${pricePerTicket}")
print(f"Total cost: ${totalCost}")