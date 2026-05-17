import random

SIZE = 5
MINES = 5

# Create empty board
board = [['-' for _ in range(SIZE)] for _ in range(SIZE)]
mine_board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

# Place mines randomly
mines = set()

while len(mines) < MINES:
    row = random.randint(0, SIZE - 1)
    col = random.randint(0, SIZE - 1)
    mines.add((row, col))

for row, col in mines:
    mine_board[row][col] = '*'

# Count nearby mines
for i in range(SIZE):
    for j in range(SIZE):

        if mine_board[i][j] == '*':
            continue

        count = 0

        for x in range(max(0, i-1), min(SIZE, i+2)):
            for y in range(max(0, j-1), min(SIZE, j+2)):
                if mine_board[x][y] == '*':
                    count += 1

        mine_board[i][j] = count


# Display board
def print_board():
    print("\nBoard:")
    for row in board:
        print(" ".join(map(str, row)))


# Game loop
while True:
    print_board()

    row = int(input("Enter row (0-4): "))
    col = int(input("Enter col (0-4): "))

    # Mine hit
    if mine_board[row][col] == '*':
        print("💥 BOOM! You hit a mine!")
        break

    # Reveal cell
    board[row][col] = mine_board[row][col]

    # Win check
    revealed = sum(cell != '-' for row in board for cell in row)

    if revealed == SIZE * SIZE - MINES:
        print_board()
        print("🎉 You won!")
        break


# Reveal final board
print("\nFinal Board:")
for row in mine_board:
    print(" ".join(map(str, row)))
