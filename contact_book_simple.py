contacts = {}

for i in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone

print("\nContact List:")
for name, phone in contacts.items():
    print(name, ":", phone)

search = input("\nSearch contact: ")
if search in contacts:
    print("Phone number:", contacts[search])
else:
    print("Contact not found")
