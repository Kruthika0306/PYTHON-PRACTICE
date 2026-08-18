visitors = 12500
orders = 875

conversion_rate = (orders / visitors) * 100

print("Website Visitors:", visitors)
print("Completed Orders:", orders)
print("Conversion Rate:", round(conversion_rate, 2), "%")

if conversion_rate >= 5:
    print("Strong conversion performance")
