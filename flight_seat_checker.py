seats = 180
booked = 162

available = seats - booked

print("Total Seats:", seats)
print("Booked:", booked)
print("Available:", available)

if available < 20:
    print("Almost Full")
