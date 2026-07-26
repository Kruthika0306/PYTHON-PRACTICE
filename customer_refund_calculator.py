order = float(input("Order amount: "))
returned = float(input("Returned items value: "))

refund = min(order, returned)
remaining = order - refund

print("Refund Amount:", refund)
print("Final Bill:", remaining)

print("Refund processed successfully")
