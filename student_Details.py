name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

mark1 = float(input("Enter marks in subject 1: "))
mark2 = float(input("Enter marks in subject 2: "))
mark3 = float(input("Enter marks in subject 3: "))

total = mark1 + mark2 + mark3

print("\n Student Details :")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Marks      :", mark1, ",", mark2, ",", mark3)
print("Total Marks:", total)