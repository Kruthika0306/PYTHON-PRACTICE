last_service = 18500
current = 24200

distance = current - last_service

print("Distance Since Service:", distance)

if distance >= 5000:
    print("Service Due")
