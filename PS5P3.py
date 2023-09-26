numBooks = int(input("Enter the number of books to order: "))
costPerBook = float(input("Enter the cost per book: "))

orderTotal = numBooks * costPerBook
shippingCharge = 0 if orderTotal > 50.0 else 25.0

print("Order Total:     ${:.2f}".format(orderTotal))
print("Shipping Charge: ${:.2f}".format(shippingCharge))