import pandas as pd

data = {"Product": ["A", "B", "C"],
        "Sales": [100, 150, 200]}

df = pd.DataFrame(data)

print(df)

total = df["Sales"].sum()
max_sale = df["Sales"].max()

print("Total Sales:", total)
print("Highest Sale:", max_sale)
