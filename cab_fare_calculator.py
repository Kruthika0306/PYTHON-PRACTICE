distance = float(input("Distance in km: "))
base_fare = 50
rate = 15

fare = base_fare + distance * rate

if distance > 20:
    fare *= 0.9

print("Distance:", distance, "km")
print("Estimated Fare:", round(fare, 2))
