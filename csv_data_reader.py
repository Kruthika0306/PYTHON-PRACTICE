import csv

file = open("data.csv", "r")
reader = csv.reader(file)

total = 0
count = 0

for row in reader:
    try:
        total += int(row[0])
        count += 1
    except:
        continue

print("Total:", total)
print("Average:", total / count if count else 0)
file.close()
