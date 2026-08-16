downtime = [12, 5, 0, 18, 7, 2]

total = sum(downtime)
average = total / len(downtime)
critical = len([x for x in downtime if x > 10])

print("Total Downtime:", total, "minutes")
print("Average Downtime:", round(average, 2))
print("Critical Incidents:", critical)
