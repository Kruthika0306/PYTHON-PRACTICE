simple_fraud_check.py
amount = float(input("Transaction amount: "))
location = input("Location: ").lower()

if amount > 50000 or location != "india":
    print("Suspicious transaction ")
else:
    print("Transaction normal ")

print("Check completed")
