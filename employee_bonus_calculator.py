salary = float(input("Salary: "))
rating = int(input("Performance Rating (1-5): "))

bonus = salary * (rating * 0.02)

print("Bonus:", bonus)
print("Total Salary:", salary + bonus)
