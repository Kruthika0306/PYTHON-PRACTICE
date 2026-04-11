from sklearn.tree import DecisionTreeClassifier

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = DecisionTreeClassifier()
model.fit(X, y)

pred = model.predict([[2.5]])

print("Prediction:", pred[0])
