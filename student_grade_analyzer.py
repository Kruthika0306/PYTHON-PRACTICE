marks = [82, 76, 91, 88, 69]

average = sum(marks) / len(marks)

print("Average:", round(average, 2))
print("Highest:", max(marks))
print("Lowest:", min(marks))

if average >= 75:
    print("Overall Performance: Good")
