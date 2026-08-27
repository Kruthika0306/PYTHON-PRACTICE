import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("news.csv")

# Remove missing values
data = data.dropna()

# News text and labels
X = data["text"]
y = data["label"]

# Convert text into numerical features
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7
)

X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Machine Learning model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Test your own news
news = input("\nEnter a news article/headline: ")

news_vector = vectorizer.transform([news])

prediction = model.predict(news_vector)

if prediction[0].lower() == "fake":
    print("\n🔴 Prediction: FAKE NEWS")
else:
    print("\n🟢 Prediction: REAL NEWS")
