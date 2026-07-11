total_requests = int(input("Total requests: "))
failed_requests = int(input("Failed requests: "))

error_rate = (failed_requests / total_requests) * 100

print("Error rate:", round(error_rate, 2), "%")

if error_rate > 5:
    print("Immediate investigation required")
else:
    print("Website performance is acceptable")

print("Status check completed")
