licenses = 120
active_users = int(input("Active users: "))

available = licenses - active_users

print("Unused Licenses:", available)

if available < 10:
    print("Purchase More Licenses")
else:
    print("License Count Sufficient")
