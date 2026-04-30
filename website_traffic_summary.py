visits = [120, 150, 90, 200, 170, 300, 250]

print("Total Visits:", sum(visits))
print("Highest Day:", max(visits))
print("Lowest Day:", min(visits))

avg = sum(visits) / len(visits)
print("Average Visits:", round(avg, 2))
