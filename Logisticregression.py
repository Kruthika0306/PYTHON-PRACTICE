import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -----------------------------
# Sample student dataset
# -----------------------------
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance":  [50, 55, 60, 65, 70, 75, 80, 85],
    "pass":        [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# Features & Target
# -----------------------------
X = df[["study_hours", "attendance"]]
y = df["pass"]

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -----------------------------
# Model
# -----------------------------
model = LogisticRegression()

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

print("\nPredictions:", y_pred)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# -----------------------------
# Predict for new student
# -----------------------------
new_student = [[6, 78]]  # study_hours, attendance

result = model.predict(new_student)

print("\nNew Student Prediction:", "Pass" if result[0] == 1 else "Fail")
