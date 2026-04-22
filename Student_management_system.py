import json
import os

FILE_NAME = "students.json"

# Load existing data
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    students = load_data()
    students.append({
        "name": name,
        "age": age,
        "course": course
    })

    save_data(students)
    print("✅ Student added successfully!")

# View students
def view_students():
    students = load_data()
    if not students:
        print("⚠️ No records found.")
        return

    print("\n📚 Student Records:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")

# Delete student
def delete_student():
    students = load_data()
    view_students()

    if not students:
        return

    try:
        index = int(input("Enter student number to delete: ")) - 1
        removed = students.pop(index)
        save_data(students)
        print(f"❌ Removed {removed['name']}")
    except (IndexError, ValueError):
        print("⚠️ Invalid input!")

# Menu
def menu():
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid choice!")

if __name__ == "__main__":
    menu()
