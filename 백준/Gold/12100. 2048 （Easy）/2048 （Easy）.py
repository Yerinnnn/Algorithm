import copy

# 격자 이동 함수
def move(board, direction):
    n = len(board)
    if direction == 0:  # 위로 이동
        for col in range(n):
            merged = [False] * n
            for row in range(1, n):
                if board[row][col] == 0:
                    continue
                current_row = row
                while current_row > 0 and board[current_row - 1][col] == 0:
                    board[current_row - 1][col] = board[current_row][col]
                    board[current_row][col] = 0
                    current_row -= 1
                if (
                    current_row > 0
                    and board[current_row - 1][col] == board[current_row][col]
                    and not merged[current_row - 1]
                ):
                    board[current_row - 1][col] *= 2
                    board[current_row][col] = 0
                    merged[current_row - 1] = True

    elif direction == 1:  # 아래로 이동
        for col in range(n):
            merged = [False] * n
            for row in range(n - 2, -1, -1):
                if board[row][col] == 0:
                    continue
                current_row = row
                while current_row < n - 1 and board[current_row + 1][col] == 0:
                    board[current_row + 1][col] = board[current_row][col]
                    board[current_row][col] = 0
                    current_row += 1
                if (
                    current_row < n - 1
                    and board[current_row + 1][col] == board[current_row][col]
                    and not merged[current_row + 1]
                ):
                    board[current_row + 1][col] *= 2
                    board[current_row][col] = 0
                    merged[current_row + 1] = True

    elif direction == 2:  # 왼쪽으로 이동
        for row in range(n):
            merged = [False] * n
            for col in range(1, n):
                if board[row][col] == 0:
                    continue
                current_col = col
                while current_col > 0 and board[row][current_col - 1] == 0:
                    board[row][current_col - 1] = board[row][current_col]
                    board[row][current_col] = 0
                    current_col -= 1
                if (
                    current_col > 0
                    and board[row][current_col - 1] == board[row][current_col]
                    and not merged[current_col - 1]
                ):
                    board[row][current_col - 1] *= 2
                    board[row][current_col] = 0
                    merged[current_col - 1] = True

    elif direction == 3:  # 오른쪽으로 이동
        for row in range(n):
            merged = [False] * n
            for col in range(n - 2, -1, -1):
                if board[row][col] == 0:
                    continue
                current_col = col
                while current_col < n - 1 and board[row][current_col + 1] == 0:
                    board[row][current_col + 1] = board[row][current_col]
                    board[row][current_col] = 0
                    current_col += 1
                if (
                    current_col < n - 1
                    and board[row][current_col + 1] == board[row][current_col]
                    and not merged[current_col + 1]
                ):
                    board[row][current_col + 1] *= 2
                    board[row][current_col] = 0
                    merged[current_col + 1] = True
    return board


# DFS 탐색
def dfs(board, depth):
    if depth == 5:  # 최대 이동 횟수 도달
        return max(max(row) for row in board)

    max_block = 0
    for direction in range(4):  # 4방향 모두 시도
        new_board = move(copy.deepcopy(board), direction)
        max_block = max(max_block, dfs(new_board, depth + 1))
    return max_block


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = dfs(board, 0)
print(result)