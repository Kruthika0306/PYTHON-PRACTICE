expenses = {
    "Food": 3200,
    "Travel": 1800,
    "Shopping": 4500,
    "Bills": 2500
}

highest = max(expenses, key=expenses.get)

for category, amount in expenses.items():
    print(category, ":", amount)

print("Highest Expense:", highest)
