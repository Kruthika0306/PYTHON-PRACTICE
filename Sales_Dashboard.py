import pandas as pd
import matplotlib.pyplot as plt

sales = {
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Revenue":[12000,15000,18000,17000,22000,25000]
}

df = pd.DataFrame(sales)

plt.figure(figsize=(8,5))
plt.plot(df["Month"],df["Revenue"],marker='o')

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid()

plt.show()
