invoices = {
    "INV001": 5,
    "INV002": 0,
    "INV003": 12
}

for invoice, days in invoices.items():
    if days > 0:
        print(invoice, "Overdue by", days, "days")
    else:
        print(invoice, "Paid on time")

print("Invoice review completed")
