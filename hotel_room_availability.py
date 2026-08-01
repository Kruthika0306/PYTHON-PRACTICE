rooms = {
    "Single": 8,
    "Double": 3,
    "Suite": 1
}

for room, available in rooms.items():
    print(room, "-", available, "rooms")

if rooms["Suite"] == 0:
    print("No Suites Available")
