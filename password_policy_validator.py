password = input("Enter password: ")

checks = [
    len(password) >= 8,
    any(c.isupper() for c in password),
    any(c.isdigit() for c in password),
    any(not c.isalnum() for c in password)
]

print("Policy Score:", sum(checks), "/4")
print("Valid Password" if all(checks) else "Invalid Password")
