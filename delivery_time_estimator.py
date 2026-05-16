distance = float(input("Enter distance (km): "))
speed = float(input("Average speed (km/h): "))

time = distance / speed

print("Estimated delivery time:",
      round(time, 2), "hours")

if time > 5:
    print("Delayed delivery ")
else:
    print("Delivery on time ")
