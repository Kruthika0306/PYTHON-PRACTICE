import pandas as pd
from sklearn.linear_model import LinearRegression

# Student dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "marks": [25, 30, 40, 50, 55, 65, 75, 85]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["study_hours"]]
y = df["marks"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks for a student who studies 9 hours
predicted_marks = model.predict([[9]])

print("Predicted Marks:", predicted_marks[0])
