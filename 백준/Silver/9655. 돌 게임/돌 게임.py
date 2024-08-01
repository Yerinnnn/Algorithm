def stone_game_winner(n):
    if n % 2 == 0:
        return "CY"
    else:
        return "SK"

N = int(input())

print(stone_game_winner(N))