employees = {
    "Aman": 45000,
    "Riya": 62000,
    "John": 38000,
    "Neha": 71000
}

total = sum(employees.values())
average = total / len(employees)

print("Total Payroll:", total)
print("Average Salary:", round(average, 2))
