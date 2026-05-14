uptime = [99.9, 99.5, 98.7, 99.8]

avg = sum(uptime) / len(uptime)

print("Average uptime:", round(avg, 2), "%")

if avg >= 99:
    print("System stable ")
else:
    print("Server issues detected ")

print("Monitoring complete")
