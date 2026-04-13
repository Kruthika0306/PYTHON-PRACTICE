from sklearn.metrics import accuracy_score

y_true = [1,0,1,1,0]
y_pred = [1,0,0,1,0]

acc = accuracy_score(y_true, y_pred)

print("Accuracy:", acc)

if acc > 0.8:
    print("Good model")
else:
    print("Needs improvement")
