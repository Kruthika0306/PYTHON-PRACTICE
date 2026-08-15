orders = [320, 450, 280, 700, 520]

total = sum(orders)
average = total / len(orders)
large_orders = len([x for x in orders if x > 500])

print("Total Orders:", len(orders))
print("Average Order:", round(average, 2))
print("Large Orders:", large_orders)
