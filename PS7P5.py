countinueProgramm = "Yes"
discountSum = 0

while countinueProgramm == "Yes":
    countinueProgramm = input("Do you want to continue (Yes/No)? ")

    if countinueProgramm != "Yes":
        break

    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    extendedPrice = quantity * price
    discountPercent = 0.1 

    if extendedPrice > 10000:
        discountPercent = 0.25 

    discount = extendedPrice * discountPercent
    total = extendedPrice - discount

    print("Extended Price:", extendedPrice)
    print("Discount Amount:", discount)
    print("Total:", total)

    discountSum += discount

print("Sum of all discounts:", discountSum)
