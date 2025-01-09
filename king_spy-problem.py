import random
import time

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
    print()

def initialize_game(grid_size):
    matrix = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    # Place the king
    king_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    matrix[king_pos[0]][king_pos[1]] = "K"

    # Place the spies
    spy1_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    while spy1_pos == king_pos:
        spy1_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    matrix[spy1_pos[0]][spy1_pos[1]] = "S"

    spy2_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    while spy2_pos == king_pos or spy2_pos == spy1_pos:
        spy2_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    matrix[spy2_pos[0]][spy2_pos[1]] = "S"

    # Place a treasure
    treasure_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    while treasure_pos == king_pos or treasure_pos == spy1_pos or treasure_pos == spy2_pos:
        treasure_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    matrix[treasure_pos[0]][treasure_pos[1]] = "T"

    return matrix, king_pos, spy1_pos, spy2_pos, treasure_pos

def move_king(king_pos, grid_size):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_moves = []
    for move in moves:
        new_x, new_y = king_pos[0] + move[0], king_pos[1] + move[1]
        if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
            valid_moves.append((new_x, new_y))
    return random.choice(valid_moves) if valid_moves else king_pos

def move_spy(spy_pos, target_pos, grid_size):
    dx = target_pos[0] - spy_pos[0]
    dy = target_pos[1] - spy_pos[1]

    new_x = spy_pos[0] + (1 if dx > 0 else -1 if dx < 0 else 0)
    new_y = spy_pos[1] + (1 if dy > 0 else -1 if dy < 0 else 0)

    if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
        return (new_x, new_y)
    return spy_pos

def main():
    grid_size = 7
    matrix, king_pos, spy1_pos, spy2_pos, treasure_pos = initialize_game(grid_size)
    treasure_collected = False

    while True:
        # Clear the board
        matrix = [["." for _ in range(grid_size)] for _ in range(grid_size)]

        # Move the king
        king_pos = move_king(king_pos, grid_size)
        if king_pos == treasure_pos:
            treasure_collected = True
            treasure_pos = None

        matrix[king_pos[0]][king_pos[1]] = "K"

        # Move the spies
        spy1_pos = move_spy(spy1_pos, king_pos, grid_size)
        spy2_pos = move_spy(spy2_pos, king_pos, grid_size)

        # Check if spies catch the king
        if spy1_pos == king_pos or spy2_pos == king_pos:
            print("The spies caught the king! Game over.")
            break

        # Place the treasure if not collected
        if not treasure_collected and treasure_pos:
            matrix[treasure_pos[0]][treasure_pos[1]] = "T"

        # Place the spies
        matrix[spy1_pos[0]][spy1_pos[1]] = "S"
        matrix[spy2_pos[0]][spy2_pos[1]] = "S"

        # Print the board
        print_matrix(matrix)

        # Check win condition for the king
        if treasure_collected and (king_pos[0] == 0 or king_pos[0] == grid_size - 1 or king_pos[1] == 0 or king_pos[1] == grid_size - 1):
            print("The king has escaped with the treasure! You win!")
            break

        # Wait before the next move
        time.sleep(1)

if __name__ == "__main__":
    main()
