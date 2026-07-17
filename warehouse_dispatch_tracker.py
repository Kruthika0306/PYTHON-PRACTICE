orders = [12, 18, 9, 15]

dispatched = sum(orders)
average = dispatched / len(orders)

print("Orders Dispatched:", dispatched)
print("Average Per Batch:", average)

if average > 12:
    print("Warehouse performing efficiently")
