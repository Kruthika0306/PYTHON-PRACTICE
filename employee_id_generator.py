department = input("Department Code: ").upper()
number = int(input("Employee Number: "))

employee_id = department + str(number).zfill(4)

print("Generated Employee ID:")
print(employee_id)

print("ID Created Successfully")
