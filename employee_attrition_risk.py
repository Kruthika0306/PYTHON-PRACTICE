years = int(input("Years at company: "))
satisfaction = int(input("Satisfaction score (1-10): "))

if years < 2 and satisfaction < 5:
    risk = "High"
elif satisfaction < 7:
    risk = "Medium"
else:
    risk = "Low"

print("Attrition Risk:", risk)
