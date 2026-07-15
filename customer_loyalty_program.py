points = int(input("Reward points: "))

if points >= 5000:
    level = "Platinum"
elif points >= 2500:
    level = "Gold"
elif points >= 1000:
    level = "Silver"
else:
    level = "Bronze"

print("Membership Level:", level)
print("Points:", points)
