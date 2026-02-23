import secrets
import string

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

new_password = generate_password()
print(f"Generated Password: {new_password}")
