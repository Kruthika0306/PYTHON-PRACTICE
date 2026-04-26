import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1

    # Digit check
    if re.search(r"\d", password):
        strength += 1

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength result
    if strength == 5:
        return "Very Strong 💪"
    elif strength >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"


# Main program
password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)
