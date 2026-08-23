deliveries = [32, 28, 41, 35, 39]
on_time = [30, 25, 38, 32, 36]

total = sum(deliveries)
completed_on_time = sum(on_time)
performance = completed_on_time / total * 100

print("Total Deliveries:", total)
print("On-Time Deliveries:", completed_on_time)
print("Performance:", round(performance, 2), "%")
