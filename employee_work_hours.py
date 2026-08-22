hours = {
    "Aman": 42,
    "Riya": 38,
    "John": 46,
    "Neha": 40
}

for employee, worked in hours.items():
    overtime = max(worked - 40, 0)
    print(employee, "Hours:", worked)
    print("Overtime:", overtime)

print("Work hour analysis completed")
