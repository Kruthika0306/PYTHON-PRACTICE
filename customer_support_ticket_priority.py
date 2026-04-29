issue = input("Issue type: ").lower()
vip = input("VIP customer? yes/no: ").lower()

if issue == "payment" or vip == "yes":
    priority = "High"
elif issue == "delivery":
    priority = "Medium"
else:
    priority = "Low"

print("Ticket Priority:", priority)
