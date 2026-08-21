
orders = {
    "Laptop": 5,
    "Phone": 12,
    "Tablet": 7,
    "Watch": 15
}

prices = {
    "Laptop": 55000,
    "Phone": 25000,
    "Tablet": 18000,
    "Watch": 5000
}

revenue = sum(orders[p] * prices[p] for p in orders)

print("Total Revenue:", revenue)
