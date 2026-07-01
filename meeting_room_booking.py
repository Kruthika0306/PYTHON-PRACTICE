rooms = ["A101", "B202", "C303"]

room = input("Enter room name: ")

if room in rooms:
    print("Room Booked Successfully")
    rooms.remove(room)
else:
    print("Room Not Available")

print("Available Rooms:", rooms)
