budget = float(input("Monthly grocery budget: "))
spent = float(input("Amount already spent: "))

remaining = budget - spent

print("Remaining budget:", remaining)

if remaining < 0:
    print("Budget exceeded")
elif remaining < budget * 0.2:
    print("Budget is almost used")
else:
    print("Budget is under control")
