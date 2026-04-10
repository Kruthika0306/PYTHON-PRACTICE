from sklearn.model_selection import train_test_split

data = [1,2,3,4,5,6,7,8]
labels = [0,1,0,1,0,1,0,1]

X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.25)

print("Train data:", X_train)
print("Test data:", X_test)

print("Train labels:", y_train)
print("Test labels:", y_test)
