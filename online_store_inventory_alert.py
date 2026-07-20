inventory = {
    "Laptop": 5,
    "Mouse": 30,
    "Keyboard": 7
}

for item, stock in inventory.items():
    if stock < 10:
        print(item, "- Low Stock")
    else:
        print(item, "- Stock Available")

print("Inventory check completed")
