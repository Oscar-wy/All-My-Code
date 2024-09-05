orderValue = float(input("Enter Order Value: "))
overallCharge = 0
postageCharge = 0
if orderValue >= 15:
    ndDelivery = input("Do You Want To Pay For Next Day Delivery? ").lower()
    if ndDelivery == "yes":
        postageCharge += 5
else:
    postageCharge += 3.50
    ndDelivery = input("Do You Want To Pay For Next Day Delivery? ").lower()
    if ndDelivery == "yes":
        postageCharge += 5
overallCharge = postageCharge + orderValue
print("Postage Charge Is:", postageCharge)
print("Overall Charge Is:", overallCharge)