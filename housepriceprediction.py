import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("house_prices.csv")

# Display first few rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# Data Visualization
# -----------------------------

# Price Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Price"], bins=10)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# Area vs Price
plt.figure(figsize=(6,4))
plt.scatter(df["Area"], df["Price"])
plt.title("Area vs House Price")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.show()

# -----------------------------
# Prepare Data
# -----------------------------
X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Predict
# -----------------------------
y_pred = model.predict(X_test)

# Model Evaluation
print("\nMean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Predict a New House Price
new_house = [[2000, 3, 2, 5]]  # Area, Bedrooms, Bathrooms, Age
predicted_price = model.predict(new_house)

print("\nPredicted House Price: ₹{:.2f}".format(predicted_price[0]))

# -----------------------------
# Actual vs Predicted
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(y_test, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.title("Actual vs Predicted House Prices")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.show()
