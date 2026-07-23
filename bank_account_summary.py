transactions = [2500, -800, 1500, -300, 5000]

balance = sum(transactions)
credits = sum(t for t in transactions if t > 0)
debits = abs(sum(t for t in transactions if t < 0))

print("Credits:", credits)
print("Debits:", debits)
print("Closing Balance:", balance)
