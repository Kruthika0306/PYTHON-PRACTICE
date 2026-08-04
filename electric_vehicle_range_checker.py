battery = int(input("Battery Percentage: "))

range_left = battery * 4

print("Estimated Range:", range_left, "km")

if battery < 20:
    print("Recharge Soon")
