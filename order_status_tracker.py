status = input("Enter order status: ").lower()

if status == "shipped":
    print("On the way ")
elif status == "delivered":
    print("Order delivered ")
elif status == "cancelled":
    print("Order cancelled ")
else:
    print("Processing ")
