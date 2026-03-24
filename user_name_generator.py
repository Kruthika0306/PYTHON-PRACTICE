name = input("Enter name: ").lower()
year = input("Enter birth year: ")

username1 = name + year
username2 = name[:3] + year
username3 = name + str(len(name))

print("Suggestions:")
print(username1)
print(username2)
print(username3)

print("Pick your favorite ")
