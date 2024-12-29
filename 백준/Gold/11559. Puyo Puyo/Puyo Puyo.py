from collections import deque

# 상하좌우 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS로 연결된 블록 그룹 찾기
# (x, y) 위치에서 같은 색의 블록 그룹을 탐색 (방문한 블록의 좌표를 리스트로 반환)
def find_group(x, y, board, visited):
    q = deque([(x, y)])
    group = [(x, y)]
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))
                group.append((nx, ny))
    return group

# 블록 제거 (그룹에 속한 블록들을 빈 칸으로 변경)
def remove_blocks(group, board):
    for x, y in group:
        board[x][y] = '.'

# 블록을 아래로 떨어뜨림
def apply_gravity(board):
    for col in range(6):
        stack = []
        # 열의 블록들을 스택에 저장
        for row in range(12):
            if board[row][col] != '.':
                stack.append(board[row][col])
        # 스택의 블록들을 아래로 채움
        for row in range(11, -1, -1):
            if stack:
                board[row][col] = stack.pop()
            else:
                board[row][col] = '.'

# 뿌요뿌요 시뮬레이션 (연쇄 횟수를 반환)
def puyo_puyo(board):
    combo = 0

    while True:
        visited = [[False] * 6 for _ in range(12)]
        to_remove = False

        # 터질 블록 그룹 탐색
        for x in range(12):
            for y in range(6):
                if board[x][y] != '.' and not visited[x][y]:
                    group = find_group(x, y, board, visited)
                    if len(group) >= 4:  # 블록 그룹이 4개 이상인 경우
                        remove_blocks(group, board)
                        to_remove = True

        # 블록이 터지지 않으면 종료
        if not to_remove:
            break

        # 중력 적용
        apply_gravity(board)
        combo += 1

    return combo

board = [list(input().strip()) for _ in range(12)]

print(puyo_puyo(board))