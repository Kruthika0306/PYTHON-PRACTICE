# Student Performance Prediction
# Data Science Mini Project

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("student_data.csv")

# Display data
print("First 5 rows:")
print(data.head())

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Select features and target
X = data[["study_hours", "attendance"]]
y = data["final_score"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Predict score for a new student
study_hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance percentage: "))

new_student = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance]
})

predicted_score = model.predict(new_student)

print("Predicted Final Score:", round(predicted_score[0], 2))

# Visualization
plt.scatter(y_test, predictions)
plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Actual vs Predicted Student Scores")
plt.show()
