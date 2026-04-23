import random

SIZE = 5
MINES = 5

# Create board
board = [['-' for _ in range(SIZE)] for _ in range(SIZE)]
mine_positions = set()

# Place mines randomly
while len(mine_positions) < MINES:
    mine_positions.add((random.randint(0, SIZE-1), random.randint(0, SIZE-1)))

revealed = set()

def get_neighbors(r, c):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            neighbors.append((nr, nc))
    return neighbors

def count_mines(r, c):
    return sum((nr, nc) in mine_positions for nr, nc in get_neighbors(r,c))

def probability_map():
    prob = {}
    for r in range(SIZE):
        for c in range(SIZE):
            if (r,c) not in revealed:
                prob[(r,c)] = MINES / (SIZE*SIZE)
    return prob

def choose_cell():
    prob = probability_map()
    return min(prob, key=prob.get)

# Game loop
for _ in range(10):
    r, c = choose_cell()

    if (r, c) in mine_positions:
        print("💥 Hit a mine at", (r,c))
        break

    revealed.add((r,c))
    board[r][c] = str(count_mines(r,c))

    for row in board:
        print(" ".join(row))
    print()
