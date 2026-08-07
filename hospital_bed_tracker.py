beds = 250
occupied = 218

available = beds - occupied

print("Occupied Beds:", occupied)
print("Available Beds:", available)

if available < 25:
    print("Hospital Near Full Capacity")
