total = int(input("Total classes held: "))
attended = int(input("Classes attended: "))

percent = (attended / total) * 100

print("Attendance:", round(percent, 2), "%")

if percent >= 75:
    print("Eligible for exam ")
else:
    print("Shortage of attendance ")
