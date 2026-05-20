products = {
    "Milk": 2,
    "Bread": 5,
    "Juice": 12
}

for item, days in products.items():
    if days <= 3:
        print(item, "- Expiring Soon")
    else:
        print(item, "- Safe")

print("Expiry check completed")
