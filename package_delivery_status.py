packages = {
    "PK101": "Delivered",
    "PK102": "In Transit",
    "PK103": "Out for Delivery"
}

for package, status in packages.items():
    print(package, "-", status)

print("Delivery status updated")
