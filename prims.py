# Prim's Algorithm in Python

def prims(graph, n):
    selected = [False] * n   # Track selected vertices
    selected[0] = True       # Start from vertex 0

    edges = 0
    print("Edge : Weight\n")

    # Loop until we get n-1 edges
    while edges < n - 1:
        minimum = float('inf')
        x = 0
        y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        edges += 1


# Number of vertices
n = 5

# Adjacency Matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Call function
prims(graph, n)
