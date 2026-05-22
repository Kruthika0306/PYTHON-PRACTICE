# Python Shopping Cart

cart = []
total = 0

while True:
    item = input("Enter item name (or type 'done' to finish): ")

    if item.lower() == "done":
        break

    price = float(input(f"Enter price of {item}: ₹"))

    cart.append((item, price))

print("\n====== SHOPPING CART ======")

for item, price in cart:
    print(f"{item} - ₹{price}")
    total += price

print(f"\nTotal Bill: ₹{total}")
print("Thank you for shopping!")
