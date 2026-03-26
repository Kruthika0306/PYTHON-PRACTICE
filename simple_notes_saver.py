note = input("Write your note: ")

file = open("notes.txt", "a")
file.write(note + "\n")
file.close()

print("Note saved!")

file = open("notes.txt", "r")
print("\nAll Notes:")
print(file.read())
file.close()
