import pandas as pd

data = {"Name": ["A", "B", "C", "D"],
        "Marks": [85, 40, 75, 30]}

df = pd.DataFrame(data)

passed = df[df["Marks"] >= 50]

print("All Data:\n", df)
print("\nPassed Students:\n", passed)

print("Count Passed:", len(passed))
