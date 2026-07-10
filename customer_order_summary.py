orders = [799, 1200, 450, 950, 1500]

total = sum(orders)
average = total / len(orders)
large_orders = [order for order in orders if order >= 1000]

print("Total revenue:", total)
print("Average order value:", round(average, 2))
print("Large orders:", len(large_orders))
print("Highest order:", max(orders))
