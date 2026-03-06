def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


matrix = [[1, 2, 3],
          [4, 5, 6]]

print("Transpose:")
for row in transpose(matrix):
    print(row)
