customers = {
    "Asha": 1200,
    "Rohan": 0,
    "Meera": 850
}

for name, due in customers.items():
    if due > 0:
        print(name, "has pending payment:", due)
    else:
        print(name, "has no pending payment")

print("Reminder check completed")
