capacity = 100
registered = int(input("Registered participants: "))

available = capacity - registered
fill_rate = (registered / capacity) * 100

print("Available seats:", available)
print("Registration fill rate:", fill_rate, "%")

if available <= 0:
    print("Registration closed")
else:
    print("Registration open")
