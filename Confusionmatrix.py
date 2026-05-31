from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)

# Actual values
y_true = [1, 0, 1, 1, 0, 1, 0, 0]

# Predicted values
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]

# Accuracy
accuracy = accuracy_score(y_true, y_pred)

# Precision
precision = precision_score(y_true, y_pred)

# Recall
recall = recall_score(y_true, y_pred)

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)

print("\nConfusion Matrix:")
print(cm)
