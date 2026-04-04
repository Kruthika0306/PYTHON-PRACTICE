principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = int(input("Enter time in years: "))

amount = principal * (1 + rate/100) ** time

print("\n--- Loan Details ---")
print("Loan Amount      :", principal)
print("Interest Rate(%) :", rate)
print("Time (years)     :", time)
print("Final Amount to be Paid:", amount)