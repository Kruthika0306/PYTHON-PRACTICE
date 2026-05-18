from collections import deque

# Maze
# 0 = path
# 1 = wall

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

ROWS = len(maze)
COLS = len(maze[0])

# Directions: up, down, left, right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# BFS function
def solve_maze(start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        # Reached destination
        if (x, y) == end:
            return path

        # Skip visited
        if (x, y) in visited:
            continue

        visited.add((x, y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < ROWS and
                0 <= ny < COLS and
                maze[nx][ny] == 0):

                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


start = (0, 0)
end = (4, 4)

path = solve_maze(start, end)

# Display result
if path:
    print("✅ Path Found:")
    print(path)
else:
    print("❌ No Path Found")
