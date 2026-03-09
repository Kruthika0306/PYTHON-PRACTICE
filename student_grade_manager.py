marks = []

for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)

avg = sum(marks) / len(marks)

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
else:
    grade = "C"

print("Average:", avg)
print("Grade:", grade)
