import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
data = {
    "Email": [
        "Congratulations! You won a free iPhone",
        "Meeting at 3 PM tomorrow",
        "Claim your free gift now",
        "Your order has been shipped",
        "Win cash prizes instantly",
        "Project submission deadline is today",
        "Exclusive offer just for you",
        "Let's have lunch tomorrow",
        "Limited time discount available",
        "Happy Birthday! Have a great day"
    ],
    "Label": [
        "Spam",
        "Ham",
        "Spam",
        "Ham",
        "Spam",
        "Ham",
        "Spam",
        "Ham",
        "Spam",
        "Ham"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Labels
X = df["Email"]
y = df["Label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Test your own email
email = ["Congratulations! You have won a lottery worth $1000"]
email_vector = vectorizer.transform(email)

prediction = model.predict(email_vector)

print("Prediction:", prediction[0])
