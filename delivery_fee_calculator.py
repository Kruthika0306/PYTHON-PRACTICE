order_amount = float(input("Order amount: "))
distance = float(input("Delivery distance in km: "))

fee = 40 + (distance * 8)

if order_amount >= 1000:
    fee = 0
elif order_amount >= 500:
    fee -= 20

print("Delivery fee:", max(fee, 0))
print("Order total:", order_amount + max(fee, 0))
