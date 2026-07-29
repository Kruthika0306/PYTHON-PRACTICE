attendance = {
    "Aman": 25,
    "Neha": 22,
    "Rahul": 27
}

for employee, days in attendance.items():
    print(employee, "worked", days, "days")

best = max(attendance, key=attendance.get)
print("Best Attendance:", best)
