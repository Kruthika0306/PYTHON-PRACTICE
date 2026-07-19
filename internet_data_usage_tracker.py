daily_usage = [2.5, 3.2, 4.1, 1.8, 2.9]

total = sum(daily_usage)
average = total / len(daily_usage)

print("Total Usage:", total, "GB")
print("Average Usage:", round(average, 2), "GB")

print("Highest Usage:", max(daily_usage), "GB")
