leave_days = int(input("Requested leave days: "))
balance = int(input("Available leave balance: "))

if leave_days <= 0:
    print("Invalid leave request")
elif leave_days <= balance:
    print("Leave approved")
    print("Remaining balance:", balance - leave_days)
else:
    print("Leave rejected: insufficient balance")

print("Request processed")
