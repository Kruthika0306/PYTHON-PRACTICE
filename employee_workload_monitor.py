tasks = {
    "Alice": 8,
    "Bob": 15,
    "Chris": 11
}

for employee, count in tasks.items():
    status = "Overloaded" if count > 12 else "Balanced"
    print(employee, "-", status)

print("Workload review completed")
