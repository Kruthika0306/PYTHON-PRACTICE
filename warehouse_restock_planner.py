inventory = {
    "Laptop": 4,
    "Keyboard": 12,
    "Monitor": 2
}

for item, stock in inventory.items():
    if stock <= 5:
        print(item, "needs restocking")
    else:
        print(item, "stock level is sufficient")

print("Restock planning completed")
