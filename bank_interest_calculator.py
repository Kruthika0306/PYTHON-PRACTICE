
principal = float(input("Principal: "))
rate = 6.5
years = int(input("Years: "))

interest = (principal * rate * years) / 100

print("Interest:", interest)
print("Final Amount:", principal + interest)
