transactions = [500, 1200, 85000, 3000, 150000]

for amount in transactions:
    if amount > 50000:
        print("Suspicious Transaction:", amount)
    else:
        print("Normal Transaction:", amount)

high_risk = len([t for t in transactions if t > 50000])
print("High Risk Transactions:", high_risk)
