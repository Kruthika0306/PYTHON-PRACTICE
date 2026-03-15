students = {}

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records:")
for name, marks in students.items():
    print(name, ":", marks)

top = max(students, key=students.get)
print("Top student:", top)
