data = [12, 45, 23, 67, 34, 89]

print("Data:", data)
print("Max:", max(data))
print("Min:", min(data))

avg = sum(data) / len(data)
print("Average:", avg)

above_avg = [x for x in data if x > avg]
print("Above average:", above_avg)
