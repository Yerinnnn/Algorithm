from collections import deque

N = int(input())
board = [list(input()) for _ in range(N)]

# 통나무와 목적지 위치 찾기
B = []  # 통나무 위치
E = []  # 목적지 위치
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            B.append((i, j))
            board[i][j] = '0'
        elif board[i][j] == 'E':
            E.append((i, j))
            board[i][j] = '0'

# 통나무가 가로인지 세로인지 확인
is_horizontal = B[0][0] == B[1][0]

# 방문 체크 (위치, 방향)
visited = set()

def can_move(pos, direction):
    # 이동 가능한지 체크하는 함수
    for x, y in pos:
        if not (0 <= x < N and 0 <= y < N) or board[x][y] == '1':
            return False
    return True

def get_next_positions(pos, is_h):
    result = []
    x, y = pos[1]  # 중심점
    
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        new_pos = []
        for px, py in pos:
            new_pos.append((px + dx[i], py + dy[i]))
        if can_move(new_pos, is_h):
            result.append((new_pos, is_h))
    
    # 회전
    if is_valid_rotation(pos):
        rotated = rotate(pos)
        if can_move(rotated, not is_h):
            result.append((rotated, not is_h))
    
    return result

def is_valid_rotation(pos):
    x, y = pos[1]  # 중심점
    # 3x3 영역 체크
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (0 <= i < N and 0 <= j < N) or board[i][j] == '1':
                return False
    return True

def rotate(pos):
    x, y = pos[1]  # 중심점
    result = []
    for px, py in pos:
        nx = x + (py - y)
        ny = y - (px - x)
        result.append((nx, ny))
    return sorted(result)

# BFS
q = deque([(B, is_horizontal, 0)])  # 위치, 방향, 이동 횟수
visited.add((tuple(B), is_horizontal))

while q:
    pos, is_h, count = q.popleft()
    
    # 목적지 도착 체크
    if sorted(pos) == sorted(E):
        print(count)
        break
        
    # 다음 위치들 탐색
    for next_pos, next_h in get_next_positions(pos, is_h):
        next_pos = tuple(sorted(next_pos))
        if (next_pos, next_h) not in visited:
            visited.add((next_pos, next_h))
            q.append((next_pos, next_h, count + 1))
else:
    print(0)