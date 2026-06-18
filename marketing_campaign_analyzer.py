clicks = 1200
visitors = 15000

ctr = (clicks / visitors) * 100

print("Click Through Rate:", round(ctr, 2), "%")

if ctr > 5:
    print("Campaign Performing Well")
else:
    print("Campaign Needs Improvement")
