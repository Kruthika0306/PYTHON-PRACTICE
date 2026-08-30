import numpy as np

# -----------------------------
# 1D Array
# -----------------------------
array1 = np.array([1, 2, 3, 4, 5])

print("1D Array:")
print(array1)

# -----------------------------
# 2D Array
# -----------------------------
array2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(array2)

# -----------------------------
# 3D Array
# -----------------------------
array3 = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Array:")
print(array3)

# -----------------------------
# Array of Zeros
# -----------------------------
zeros = np.zeros((3, 3))

print("\nZero Array:")
print(zeros)

# -----------------------------
# Array of Ones
# -----------------------------
ones = np.ones((2, 4))

print("\nOnes Array:")
print(ones)

# -----------------------------
# Identity Matrix
# -----------------------------
identity = np.eye(3)

print("\nIdentity Matrix:")
print(identity)

# -----------------------------
# Random Array
# -----------------------------
random_array = np.random.randint(1, 100, (3, 3))

print("\nRandom Array:")
print(random_array)

# -----------------------------
# Diagonal Array
# -----------------------------
diag = np.diag([1, 2, 3, 4])

print("\nDiagonal Matrix:")
print(diag)
