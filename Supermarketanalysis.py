import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("supermarket_sales.csv")

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

# Total Revenue
print("Total Revenue: ₹", df["Revenue"].sum())

# Best-selling Product
best_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("Best Selling Product:", best_product)

# Revenue by Category
category_sales = df.groupby("Category")["Revenue"].sum()

# Revenue by Payment Method
payment_sales = df.groupby("Payment")["Revenue"].sum()

# Average Rating
print("Average Rating:", round(df["Rating"].mean(), 2))

# -----------------------------
# Bar Chart - Revenue by Category
# -----------------------------
category_sales.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# -----------------------------
# Pie Chart - Payment Methods
# -----------------------------
payment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue by Payment Method")
plt.ylabel("")
plt.tight_layout()
plt.savefig("payment_methods.png")
plt.show()

# -----------------------------
# Histogram - Ratings
# -----------------------------
plt.hist(df["Rating"], bins=5)
plt.title("Customer Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("ratings_distribution.png")
plt.show()

# -----------------------------
# Revenue by Product
# -----------------------------
product_sales = df.groupby("Product")["Revenue"].sum()

product_sales.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("product_revenue.png")
plt.show()
