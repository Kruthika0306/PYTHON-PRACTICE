orders = {
    "Packed": 18,
    "Shipped": 25,
    "Delivered": 40
}

total = sum(orders.values())

for status, count in orders.items():
    print(status, ":", count)

print("Total Orders:", total)
