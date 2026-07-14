invoices = {
    "INV101": "Paid",
    "INV102": "Pending",
    "INV103": "Paid",
    "INV104": "Pending"
}

pending = 0

for invoice, status in invoices.items():
    print(invoice, "-", status)
    if status == "Pending":
        pending += 1

print("Pending Invoices:", pending)
