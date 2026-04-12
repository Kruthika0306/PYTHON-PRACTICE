from sklearn.preprocessing import MinMaxScaler

data = [[10],[20],[30],[40]]

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)

print("Original:", data)
print("Scaled:", scaled)

print("Done normalization")
