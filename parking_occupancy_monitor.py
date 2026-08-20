total_slots = 120
occupied_slots = [85, 92, 101, 110]

for occupied in occupied_slots:
    available = total_slots - occupied
    rate = (occupied / total_slots) * 100
    print("Occupied:", occupied, "Available:", available)
    print("Occupancy Rate:", round(rate, 2), "%")

print("Parking analysis completed")