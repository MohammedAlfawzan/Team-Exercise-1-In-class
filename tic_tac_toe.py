def check_winner(game_state):
    # Check horizontal lines
    for row in game_state:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # Check vertical lines
    for col in range(3):
        if game_state[0][col] == game_state[1][col] == game_state[2][col] != 0:
            return game_state[0][col]

    # Check diagonals
    if game_state[0][0] == game_state[1][1] == game_state[2][2] != 0:
        return game_state[0][0]
    if game_state[0][2] == game_state[1][1] == game_state[2][0] != 0:
        return game_state[0][2]

    # No winner
    return 0
