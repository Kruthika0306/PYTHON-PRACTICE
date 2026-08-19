waiting_times = [18, 25, 12, 40, 31, 15]

average = sum(waiting_times) / len(waiting_times)
long_waits = len([x for x in waiting_times if x > 30])

print("Average Waiting Time:", round(average, 2), "minutes")
print("Long Waiting Cases:", long_waits)

if average > 25:
    print("Waiting time needs improvement")
