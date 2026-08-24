crashes = {
    "Android": 42,
    "iOS": 18,
    "Web": 7
}

total = sum(crashes.values())
platform = max(crashes, key=crashes.get)

print("Total Crashes:", total)
print("Highest Crash Platform:", platform)

for name, count in crashes.items():
    print(name, ":", count)
