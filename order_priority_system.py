orders = {
    "ORD101": 1200,
    "ORD102": 450,
    "ORD103": 3200,
    "ORD104": 800
}

for order, amount in orders.items():
    priority = "High" if amount > 2000 else "Normal"
    print(order, "-", priority)

print("Order priority analysis completed")
