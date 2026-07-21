distance = float(input("Distance travelled (km): "))
fuel = float(input("Fuel used (litres): "))

efficiency = distance / fuel

print("Mileage:", round(efficiency, 2), "km/l")

if efficiency > 18:
    print("Fuel efficient vehicle")
else:
    print("Fuel efficiency can be improved")
